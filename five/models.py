from django.db import models

class Geocache(models.Model):
    guid = models.CharField(max_length=254, blank=True, null=True, unique=True)
    order = models.IntegerField()

    # Coordinates
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)

    # Solutions
    solutions = models.CharField(max_length=2)

    # Found?
    name = models.CharField(max_length=255, null=True)
    ip = models.GenericIPAddressField(null=True)
    found_on = models.DateTimeField(null=True)

    @property
    def is_found(self):
        return (self.name != None)