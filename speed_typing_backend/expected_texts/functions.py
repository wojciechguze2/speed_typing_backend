import random

from speed_typing_backend.authors.models import Author
from speed_typing_backend.expected_texts.models import ExpectedText
from speed_typing_backend.globals.models import Locale
from speed_typing_backend.openai_integration.integration import translate, get_opensource_text
from speed_typing_backend.settings import OPENAI_SECRET_KEY


def translate_text(text: ExpectedText, locale: Locale):
    return translate(text.text, locale.iso)


def translate_texts():
    texts_to_translate = ExpectedText.objects.filter(
        expectedtext__isnull=True,  # child not defined = texts not translated yet
        locale_id=Locale.DEFAULT_LOCALE_ID
    )

    for text_to_translate in texts_to_translate:
        for locale in Locale.objects.filter(id__in=[Locale.ENGLISH_LOCALE_ID, Locale.GERMAN_LOCALE_ID]):
            translation = translate_text(text_to_translate, locale)

            ExpectedText.objects.create(
                text=translation,
                author=text_to_translate.author,
                locale_id=locale.id,
                active=True,
                original_text=text_to_translate
            )


def create_texts_from_generator():
    if not OPENAI_SECRET_KEY:
        return None

    topics = [
        'literatura lub dowolna',
        'sztuka lub dowolna',
        None
    ]

    authors = Author.objects.all()

    for _ in range(50):
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

        print(text)

        if created:
            for locale in Locale.objects.filter(id__in=[Locale.ENGLISH_LOCALE_ID, Locale.GERMAN_LOCALE_ID]):
                translation = translate_text(expected_text, locale)

                ExpectedText.objects.create(
                    text=translation,
                    author=author,
                    locale_id=locale.id,
                    active=True,
                    original_text=expected_text
                )
