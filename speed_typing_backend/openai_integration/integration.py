import random

import openai

from speed_typing_backend.authors.models import Author
from speed_typing_backend.expected_texts.models import ExpectedText
from speed_typing_backend.globals.models import Locale
from speed_typing_backend.openai_integration.exceptions import TranslationError
from speed_typing_backend.settings import OPENAI_SECRET_KEY
from speed_typing_backend.translations.models import TranslationBase, Translation


def translate(text: str, target_locale_iso: str, max_tokens=254):
    if not OPENAI_SECRET_KEY:
        raise TranslationError

    openai.api_key = OPENAI_SECRET_KEY

    source_locale = 'polskiego'
    target_locale = None

    if target_locale_iso == 'en':
        target_locale = 'angielski'
    elif target_locale_iso == 'de':
        target_locale = 'niemiecki'

    if not target_locale:
        raise TranslationError

    if target_locale:
        prompt = f"Przetłumacz z {source_locale} na {target_locale} tekst: '{text}'"

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=0.25,
            stop=None
        )

        translation = response.choices[0].text.strip().replace('"', '').replace("'", '')

        if not translation:
            raise TranslationError

        """
        print('prompt:', prompt, '\n' 't:', translation)
        print()
        """

        return translation


def get_opensource_text(author_name: [str, None], topic: str = 'dowolna', max_chars: int = 254):
    if not OPENAI_SECRET_KEY:
        raise TranslationError

    openai.api_key = OPENAI_SECRET_KEY

    prompt = 'Wygeneruj w języku polskim tekst'

    """
    if author_name:
        prompt += ' autora o nazwie: %s' % author_name
    """

    if topic:
        prompt += ' o kategorii: %s' % topic

    if max_chars:
        prompt += ' (maksymalna ilość znaków: %d)' % max_chars

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=max_chars,
        temperature=0.9,
        stop=None
    )

    text = response.choices[0].text.strip()

    if not text.endswith('.'):
        last_dot_index = text.rfind('.')

        if last_dot_index != -1:
            text = text[:last_dot_index + 1]

    return text


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


def translate_expected_text(text: ExpectedText, locale: Locale):
    return translate(text.text, locale.iso)


def translate_expected_texts():
    texts_to_translate = ExpectedText.objects.filter(
        expectedtext__isnull=True,  # child not defined = texts not translated yet
        locale_id=Locale.DEFAULT_LOCALE_ID
    )

    for text_to_translate in texts_to_translate:
        for locale in Locale.objects.filter(id__in=[Locale.ENGLISH_LOCALE_ID, Locale.GERMAN_LOCALE_ID]):
            translation = translate_expected_text(text_to_translate, locale)

            ExpectedText.objects.create(
                text=translation,
                author=text_to_translate.author,
                locale_id=locale.id,
                active=True,
                original_text=text_to_translate
            )


def create_expected_texts():
    if not OPENAI_SECRET_KEY:
        return None

    topics = [
        'literatura lub dowolna',
        'sztuka lub dowolna',
        None
    ]

    authors = Author.objects.all()

    for _ in range(2):
        author = random.choice([random.choice(authors), None])

        text = get_opensource_text(author.name if author else None, random.choice(topics))

        if not text:
            continue

        expected_text, created = ExpectedText.objects.get_or_create(
            text=text,
            defaults=dict(
                author=author,
                locale_id=Locale.DEFAULT_LOCALE_ID
            )
        )

        if created:
            for locale in Locale.objects.filter(id__in=[Locale.ENGLISH_LOCALE_ID, Locale.GERMAN_LOCALE_ID]):
                translation = translate_expected_text(expected_text, locale)

                ExpectedText.objects.create(
                    text=translation,
                    author=author,
                    locale_id=locale.id,
                    active=True,
                    original_text=expected_text
                )
