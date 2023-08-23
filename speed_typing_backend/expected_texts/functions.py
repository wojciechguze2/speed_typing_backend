import random

from django.db.models import QuerySet
from django.db.models.functions import Length

from speed_typing_backend.authors.models import Author
from speed_typing_backend.expected_texts.models import ExpectedText
from speed_typing_backend.game_modes.models import GameMode, GameModeDefaultTimeLimits, GameModeType
from speed_typing_backend.globals.models import Locale
from speed_typing_backend.openai_integration.integration import translate, get_opensource_text
from speed_typing_backend.settings import OPENAI_SECRET_KEY


def default_filter_expected_texts_by_game_mode(
        game_mode: GameMode,
        expected_texts: [QuerySet[ExpectedText], None],
        time_limit_seconds: int
) -> QuerySet[ExpectedText]:
    if expected_texts is None:
        expected_texts = ExpectedText.objects.filter(active=True)

    if not expected_texts.exists():
        return expected_texts

    if game_mode.gamemodegamemodetype_set.filter(
            game_mode_type__code=GameModeType.GAME_MODE_TYPE_TEXT_LENGTH
    ).exists():
        expected_texts = expected_texts.annotate(text_length=Length('text'))

    if game_mode.code == GameMode.GAME_MODE_LONG_TEXT_CODE:
        expected_texts = expected_texts.filter(text_length__gte=256)
    elif game_mode.code == GameMode.GAME_MODE_FAST_GAME_CODE:
        expected_texts = expected_texts.filter(text_length__lte=256)
    elif game_mode.code == GameMode.GAME_MODE_TIME_LIMIT_CODE:
        if not time_limit_seconds:
            time_limit_seconds = random.choice(GameModeDefaultTimeLimits.DEFAULT_TIME_LIMITS)

        default_time_limit = GameModeDefaultTimeLimits.objects.filter(
            time_limit_seconds=time_limit_seconds
        ).order_by('?').first()
        max_chars = default_time_limit.max_chars
        expected_texts = expected_texts.filter(text_length__lte=max_chars)

    return expected_texts


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
