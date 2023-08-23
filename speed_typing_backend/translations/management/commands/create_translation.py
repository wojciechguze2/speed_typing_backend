from abc import ABC

from django.core.management import BaseCommand

from speed_typing_backend.globals.models import Locale
from speed_typing_backend.translations.models import TranslationBase, Translation


class Command(BaseCommand, ABC):
    def handle(self, *args, **kwargs):
        translation_code = input('code: ').strip()

        locales = Locale.objects.all()
        translations = []

        for locale in locales:
            translation = input('%s: ' % locale.iso.upper()).strip()

            translations.append({
                'locale_id': locale.id,
                'translation': translation
            })

        translation_base, _ = TranslationBase.objects.get_or_create(
            code=translation_code
        )

        for translation_el in translations:
            locale_id = translation_el['locale_id']
            translation = translation_el['translation']

            if translation:
                Translation.objects.get_or_create(
                    base=translation_base,
                    locale_id=locale_id,
                    defaults=dict(
                        translation=translation
                    )
                )

        print('success')