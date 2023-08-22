from speed_typing_backend.globals.models import Locale
from speed_typing_backend.openai_integration.integration import translate
from speed_typing_backend.settings import OPENAI_SECRET_KEY
from speed_typing_backend.translations.models import TranslationBase, Translation


def create_translations():
    if not OPENAI_SECRET_KEY:
        return None

    base_translations = TranslationBase.objects.filter(
        translation__locale_id=Locale.DEFAULT_LOCALE_ID,
        auto_translate_enabled=True
    ).exclude(
        translation__locale_id__in=Locale.FOREIGN_LOCALE_IDS
    )

    base_translations = base_translations.filter(  # make sure it doesnt contain duplicated
        id__in=list(set(base_translations.values_list('id', flat=True)))
    )

    foreign_locales = Locale.objects.filter(
        id__in=Locale.FOREIGN_LOCALE_IDS
    )

    for base_translation in base_translations:
        default_translation = base_translation.default_translation

        for locale in foreign_locales:
            translation = translate(default_translation.translation, locale.iso, max_tokens=127)

            Translation.objects.create(
                base=base_translation,
                locale_id=locale.id,
                translation=translation
            )

