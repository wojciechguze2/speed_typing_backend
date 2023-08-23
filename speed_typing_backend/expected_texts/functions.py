import random

from django.db.models import QuerySet
from django.db.models.functions import Length

from speed_typing_backend.expected_texts.models import ExpectedText
from speed_typing_backend.game_modes.models import GameMode, GameModeDefaultTimeLimits, GameModeType


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
