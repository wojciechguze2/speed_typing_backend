from django.db import models


class GameMode(models.Model):
    code = models.CharField(max_length=255, null=False, blank=False)
