import json

from django.conf import settings
from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render
from django.template.defaultfilters import date as _date
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.utils import timezone

from .models import Guess
from .config import BOARD_HEIGHT, BOARD_WIDTH, TRIES_PER_HOUR, SQUARE_WIDTH, SQUARE_HEIGHT

from .utils import process_guess, get_ip


# Process guess
def guess(request, x, y):
    # Check if IP can make a guess
    status, key, tries_left, expires_at = process_guess(request, x, y)

    # Send this guess to everyone via WebSocket
    if status == 0:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'one',
            {
                "type": "guess",
                "x": x,
                "y": y,
                "key": key,
            }
        )

    res = {
        "status": status,
        "key": key,
        "tries_left": tries_left,
        "expires_at": _date(timezone.localtime(expires_at), "d/m/Y H:i:s") if expires_at else "",
    }
    return HttpResponse(json.dumps(res), content_type="application/json")


def list_guesses(request):
    cached_list = cache.get('all')
    if not cached_list:
        guesses = list(Guess.objects.all().values('x', 'y', 'key'))
        guesses = json.dumps(guesses)
        cache.set('all', guesses)
        cached_list = guesses

    # Calculate IP's tries_left & expires_at to send in the response
    now = timezone.now()
    ip = get_ip(request)
    tries = 0
    expires_at = None

    if ip:
        v = cache.get(ip)
        has_expired = (v and v["expires_at"] < now)
        if not v or (v and has_expired):
            if has_expired:
                cache.delete(ip)

        else:
            tries = v["tries"]
            expires_at = v["expires_at"]

    tries_left = TRIES_PER_HOUR - tries

    return HttpResponse(json.dumps({
        "guesses": cached_list,
        "tries_left": tries_left,
        "expires_at": _date(timezone.localtime(expires_at), "d/m/Y H:i:s") if expires_at else "",
    }), content_type="application/json")


def puzzle(request):
    return render(request, "1/index.html", {
        "BOARD_WIDTH": BOARD_WIDTH,
        "BOARD_HEIGHT": BOARD_HEIGHT,
        "SQUARE_WIDTH": SQUARE_WIDTH,
        "SQUARE_HEIGHT": SQUARE_HEIGHT,
        "DEBUG": settings.DEBUG,
        "title": "Challenge 1"
    })
