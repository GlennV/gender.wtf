from datetime import timedelta

from django.core.cache import cache
from django.utils import timezone

from core.utils import get_ip
from .models import Guess
from .config import BOARD_WIDTH, BOARD_HEIGHT, TRIES_PER_HOUR, SOLUTIONS


def process_guess(request, x, y):
    """
    Status codes:
    -3: x, y invalid
    -2: ip invalid
    -1: no more tries left
    0: OK
    """

    if not ((0 <= x <= BOARD_WIDTH) and (0 <= y <= BOARD_HEIGHT)):
        # Invalid X,Y
        return -3, "", None, None

    ip = get_ip(request)
    if not ip:
        # Invalid IP
        return -2, "", None, None

    now = timezone.now()
    v = cache.get(ip)
    has_expired = (v and v["expires_at"] < now)

    # Check if IP limit has expired
    if not v or (v and has_expired):
        if has_expired:
            cache.delete(ip)

        tries = 1
        expires_at = now + timedelta(hours=1)
        cache.set(ip, {
            "tries": tries,
            "expires_at": expires_at
        }, None)

    else:
        tries = v["tries"] + 1
        expires_at = v["expires_at"]

        if tries > TRIES_PER_HOUR:
            return -1, "", None, None

        cache.set(ip, {
            "tries": tries,
            "expires_at": expires_at
        }, None)

    guess = str(x) + "x" + str(y)
    key = SOLUTIONS[guess] if guess in SOLUTIONS else ""
    g, c = Guess.objects.get_or_create(x=x, y=y, key=key)
    if c and key:
        g.ip = ip
        g.save()

    # Reset cache
    cache.delete('all')

    return 0, g.key, TRIES_PER_HOUR - tries, expires_at
