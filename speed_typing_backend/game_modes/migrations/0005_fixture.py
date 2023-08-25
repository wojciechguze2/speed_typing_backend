from django.db import migrations

from speed_typing_backend.game_modes.models import GameModeDefaultTimeLimits, GameModeType, \
    GameModeGameModeType
from speed_typing_backend.game_modes.models import GameMode as GameModeConstants
from speed_typing_backend.globals.models import Locale
from speed_typing_backend.translations.models import Translation, TranslationBase


def get_translation_code(game_mode_code: str):
    return 'game_mode.%s' % game_mode_code


def add_fixture(apps, schema_editor):
    GameMode = apps.get_model('game_modes', 'GameMode')

    game_modes = [
        {
            'code': GameModeConstants.GAME_MODE_LONG_TEXT_CODE,
            'types': [GameModeType.GAME_MODE_TYPE_TEXT_LENGTH],
            'translations': {
                Locale.POLISH_LOCALE_ID: 'Długi tekst',
                Locale.ENGLISH_LOCALE_ID: 'Long text',
                Locale.GERMAN_LOCALE_ID: 'Langer Text'
            }
        },
        {
            'code': GameModeConstants.GAME_MODE_TIME_LIMIT_CODE,
            'types': [GameModeType.GAME_MODE_TYPE_TIME, GameModeType.GAME_MODE_TYPE_TEXT_LENGTH],
            'translations': {
                Locale.POLISH_LOCALE_ID: 'Limit czasu',
                Locale.ENGLISH_LOCALE_ID: 'Time limit',
                Locale.GERMAN_LOCALE_ID: 'Zeitlimit'
            }
        },
        {
            'code': GameModeConstants.GAME_MODE_BY_ONE_LETTER_CODE,
            'translations': {
                Locale.POLISH_LOCALE_ID: 'Po jednej literze',
                Locale.ENGLISH_LOCALE_ID: 'By one letter',
                Locale.GERMAN_LOCALE_ID: 'Jeweils einen Buchstaben'
            }
        },
        {
            'code': GameModeConstants.GAME_MODE_BY_ONE_WORD_CODE,
            'translations': {
                Locale.POLISH_LOCALE_ID: 'Po jednym wyrazie',
                Locale.ENGLISH_LOCALE_ID: 'By one word',
                Locale.GERMAN_LOCALE_ID: 'Jeweils ein Wort'
            }
        },
        {
            'code': GameModeConstants.GAME_MODE_MULTILANGUAGE,
            'translations': {
                Locale.POLISH_LOCALE_ID: 'Wiele języków',
                Locale.ENGLISH_LOCALE_ID: 'Multilanguage',
                Locale.GERMAN_LOCALE_ID: 'Mehrsprachigkeit'
            }
        },
    ]

    for game_mode in game_modes:
        game_mode_code: str = game_mode['code']
        game_mode_translations: dict = game_mode['translations']
        game_mode_types: [list, None] = game_mode.get('types')

        game_mode, is_created_game_mode = GameMode.objects.get_or_create(
            code=game_mode_code
        )

        if game_mode_code == GameModeConstants.GAME_MODE_MULTILANGUAGE:
            game_mode.multilanguage = True
            game_mode.save(update_fields=['multilanguage'])

        if game_mode_types:
            for game_mode_type in game_mode_types:
                game_mode_type, is_created_game_mode_type = GameModeType.objects.get_or_create(code=game_mode_type)
                GameModeGameModeType.objects.get_or_create(game_mode=game_mode, game_mode_type=game_mode_type)

        if game_mode_code == GameModeConstants.GAME_MODE_TIME_LIMIT_CODE:
            GameModeDefaultTimeLimits.objects.get_or_create(
                time_limit_seconds=180,
                max_chars=1200
            )

            GameModeDefaultTimeLimits.objects.get_or_create(
                time_limit_seconds=120,
                max_chars=800
            )

            GameModeDefaultTimeLimits.objects.get_or_create(
                time_limit_seconds=40,
                max_chars=300
            )

            GameModeDefaultTimeLimits.objects.get_or_create(
                time_limit_seconds=25,
                max_chars=150
            )

            GameModeDefaultTimeLimits.objects.get_or_create(
                time_limit_seconds=20,
                max_chars=100
            )

        translation_base, _ = TranslationBase.objects.get_or_create(
            code=get_translation_code(game_mode_code)
        )

        for locale_id, translation in game_mode_translations.items():
            Translation.objects.get_or_create(
                base=translation_base,
                locale_id=locale_id,
                defaults=dict(
                    translation=translation
                )
            )

    fast_game_mode = GameMode.objects.get(code=GameModeConstants.GAME_MODE_FAST_GAME_CODE)
    GameModeGameModeType.objects.get_or_create(
        game_mode=fast_game_mode,
        game_mode_type=GameModeType.objects.get(code=GameModeType.GAME_MODE_TYPE_TEXT_LENGTH)
    )

    game_mode_code = GameModeConstants.GAME_MODE_RANDOM

    translation_base, _ = TranslationBase.objects.get_or_create(
        code=get_translation_code(game_mode_code)
    )

    Translation.objects.get_or_create(
        base=translation_base,
        locale_id=Locale.POLISH_LOCALE_ID,
        defaults=dict(
            translation='Losowy tryb gry'
        )
    )

    Translation.objects.get_or_create(
        base=translation_base,
        locale_id=Locale.ENGLISH_LOCALE_ID,
        defaults=dict(
            translation='Random game mode'
        )
    )

    Translation.objects.get_or_create(
        base=translation_base,
        locale_id=Locale.GERMAN_LOCALE_ID,
        defaults=dict(
            translation='Zufallsspielmodus'
        )
    )


class Migration(migrations.Migration):
    dependencies = [
        ('game_modes', '0004_gamemode_multilanguage_and_more'),
    ]

    operations = [
        migrations.RunPython(add_fixture),
    ]
