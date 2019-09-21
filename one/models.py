from django.db import models
from django.core import validators
from django.db.models import GenericIPAddressField

from one.config import BOARD_WIDTH, BOARD_HEIGHT


class Guess(models.Model):
    x = models.IntegerField(validators=[validators.MinValueValidator(0), validators.MaxValueValidator(BOARD_WIDTH)])
    y = models.IntegerField(validators=[validators.MinValueValidator(0), validators.MaxValueValidator(BOARD_HEIGHT)])
    # empty (incorrect) or 1 letter
    key = models.CharField(max_length=1)

    ip = GenericIPAddressField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)
