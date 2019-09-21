from django.db import models


class SolutionTry(models.Model):
    keywords = models.TextField()
    correct_count = models.IntegerField(default=0)  # 1 to 8
    name = models.CharField(max_length=255)

    ip = models.GenericIPAddressField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)
