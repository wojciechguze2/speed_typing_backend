from django.db import models

from speed_typing_backend.globals.models import Locale


class TranslationBase(models.Model):
    code = models.CharField(max_length=127, null=False, blank=False)
    auto_translate_enabled = models.BooleanField(default=True, null=False, blank=False)

    @property
    def default_translation(self):
        default_translations = self.translation_set.filter(locale_id=Locale.DEFAULT_LOCALE_ID)

        if not default_translations.exists():
            return False

        return default_translations.first()


class Translation(models.Model):
    base = models.ForeignKey(TranslationBase, null=False, blank=False, on_delete=models.CASCADE)
    translation = models.CharField(max_length=511, null=True, blank=False)
    locale = models.ForeignKey(Locale, null=False, blank=False, default=Locale.DEFAULT_LOCALE_ID,
                               on_delete=models.SET_DEFAULT)

    def repr(self):
        return {
            self.base.code: self.translation
        }

    def repr_long(self):
        return {
            'id': self.id,
            'code': self.base.code,
            'translation': self.translation,
            'locale': self.locale.repr()
        }
