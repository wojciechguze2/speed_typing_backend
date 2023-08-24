from django.db import models


class Locale(models.Model):
    """
    iso codes: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
    """
    POLISH_LOCALE_ID = 1
    ENGLISH_LOCALE_ID = 2
    GERMAN_LOCALE_ID = 3

    DEFAULT_LOCALE_ID = POLISH_LOCALE_ID  # polish (:
    FOREIGN_LOCALE_IDS = [
        ENGLISH_LOCALE_ID,
        GERMAN_LOCALE_ID
    ]

    AVAILABLE_LANGUAGE_IDS = [DEFAULT_LOCALE_ID] + FOREIGN_LOCALE_IDS

    AVAILABLE_LANGUAGE_CODES = [
        'pl',
        'en',
        'de'
    ]

    iso = models.CharField(null=False, blank=False, max_length=15)
    name = models.CharField(null=False, blank=False, max_length=63)

    def repr(self):
        return {
            'id': self.id,
            'iso': self.iso,
            'name': self.name
        }


class StaticPage(models.Model):
    path = models.CharField(null=False, blank=False, max_length=127)
    title = models.CharField(null=False, blank=False, max_length=127)
    content = models.TextField(null=False, blank=False, max_length=255)

    def repr(self):
        return {
            'id': self.id,
            'path': self.path,
            'title': self.title
        }

    def repr_long(self):
        return {
            'id': self.id,
            'path': self.path,
            'title': self.title,
            'content': self.content
        }
