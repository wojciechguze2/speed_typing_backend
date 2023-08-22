from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from speed_typing_backend.game.models import Game
from speed_typing_backend.game_modes.models import GameMode
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
