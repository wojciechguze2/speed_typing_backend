from django.db import models


class Locale(models.Model):
    """
    iso codes: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
    """
    POLISH_LOCALE_ID = 1
    ENGLISH_LOCALE_ID = 2
    GERMAN_LOCALE_ID = 3

    DEFAULT_LOCALE_ID = POLISH_LOCALE_ID  # polish (:

    iso = models.CharField(null=False, blank=False, max_length=15)
    name = models.CharField(null=False, blank=False, max_length=63)

    def repr(self):
        return {
            'id': self.id,
            'iso': self.iso,
            'name': self.name
        }
