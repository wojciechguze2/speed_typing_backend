import random

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from speed_typing_backend.expected_texts.functions import default_filter_expected_texts_by_game_mode
from speed_typing_backend.expected_texts.models import ExpectedText
from speed_typing_backend.game.models import Game
from speed_typing_backend.game_modes.functions import get_random_game_mode
from speed_typing_backend.game_modes.models import GameMode, GameModeDefaultTimeLimits
from speed_typing_backend.globals.decorators import exception_decorator
from speed_typing_backend.users.functions import request_user


class SaveGameViewSet(ViewSet):
    @staticmethod
    @exception_decorator()
    def save(request: Request):
        try:
            user = request_user(request)
        except Exception as e:
            print(type(e))
            user = None

        expected_text_id = request.data.get('expectedTextId')
        game_mode_code = request.data.get('gameModeCode')
        cpm = request.data.get('cpm')
        time_ms = request.data.get('timeMs')
        mistakes_count = request.data.get('mistakesCount')

        game_mode = GameMode.objects.get(code=game_mode_code)

        Game.objects.create(
            user=user,
            expected_text_id=expected_text_id,
            game_mode=game_mode,
            cpm=cpm,
            time_ms=time_ms,
            mistakes_count=mistakes_count
        )

        return Response(True)


class GameExpectedTextViewSet(ViewSet):
    @staticmethod
    @exception_decorator()
    def retrieve(request: Request):
        locale_iso = request.query_params.get('locale_iso')
        game_mode_code = request.query_params.get('game_mode_code')
        expected_texts = ExpectedText.objects.filter(active=True)
        time_limit_seconds = random.choice(GameModeDefaultTimeLimits.DEFAULT_TIME_LIMITS)

        if not game_mode_code:
            game_mode_code = GameMode.GAME_MODE_RANDOM

        if game_mode_code == GameMode.GAME_MODE_RANDOM:
            game_mode = get_random_game_mode()

            expected_texts = default_filter_expected_texts_by_game_mode(
                game_mode,
                expected_texts,
                time_limit_seconds
            )
        else:
            game_mode = GameMode.objects.get(code=game_mode_code, active=True)

            if game_mode.text_assignment:
                expected_texts = expected_texts.filter(
                    gamemodeexpectedtext__game_mode=game_mode
                )
            else:
                expected_texts = default_filter_expected_texts_by_game_mode(
                    game_mode,
                    expected_texts,
                    time_limit_seconds
                )

        if locale_iso and not game_mode.multilanguage:
            expected_texts = expected_texts.filter(locale__iso=locale_iso)

        if not expected_texts.exists():
            game_mode = GameMode.GAME_MODE_FAST_GAME_CODE
            expected_texts = default_filter_expected_texts_by_game_mode(
                game_mode,
                expected_texts,
                time_limit_seconds
            )

        return Response({
            'gameModeCode': game_mode.code,
            'expectedText': expected_texts.order_by('?').first().repr(),
            'timeLimitSeconds': time_limit_seconds
        })
