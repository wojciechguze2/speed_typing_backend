from django.db import models

from speed_typing_backend.globals.models import Locale


class Translation(models.Model):
    code = models.CharField(max_length=127, null=False, blank=False)
    translation = models.CharField(max_length=254, null=True, blank=False)
    locale = models.ForeignKey(Locale, null=False, blank=False, default=Locale.DEFAULT_LOCALE_ID,
                               on_delete=models.SET_DEFAULT)

    def repr(self):
        return {
            self.code: self.translation
        }

    def repr_long(self):
        return {
            'id': self.id,
            'code': self.code,
            'translation': self.translation,
            'locale': self.locale.repr()
        }
