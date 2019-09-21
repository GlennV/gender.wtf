from django.core.management import BaseCommand

from five.models import Geocache


class Command(BaseCommand):
    def handle(self, *args, **options):
        Geocache.objects.create(
            guid="94e57235-a688-49a7-a818-8728b347b99f",
            order=1,
            lat=51.17962,
            lon=3.18974,
            solutions="dc",
        )

        Geocache.objects.create(
            guid="50aa5510-2034-4dea-bff2-15d6c765b05f",
            order=2,
            lat=51.17697,
            lon=3.19164,
            solutions="wy",
        )

        Geocache.objects.create(
            guid="a793467a-2cbc-4f98-ae76-1ebc89f60356",
            order=3,
            lat=51.17544,
            lon=3.19688,
            solutions="bq",
        )

        Geocache.objects.create(
            guid="c3b1f46f-806e-42cb-b7c1-8a472668ce13",
            order=4,
            lat=51.17958,
            lon=3.19744,
            solutions="hz",
        )

        Geocache.objects.create(
            guid="052968c7-b0a0-4928-9275-7347befb5a20",
            order=5,
            lat=51.17836,
            lon=3.19300,
            solutions="rh",
        )
