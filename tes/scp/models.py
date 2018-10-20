from django.db import models


class Information(models.Model):
    title = models.CharField(max_length=6000)
    speaker = models.CharField(max_length=6000)
    time = models.CharField(max_length=6000)
    place = models.CharField(max_length=6000)

