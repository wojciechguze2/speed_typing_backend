from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from speed_typing_backend.game_modes.models import GameMode
from speed_typing_backend.globals.decorators import exception_decorator


class GameModesViewSet(ViewSet):
    @staticmethod
    @exception_decorator()
    def list(request: Request) -> Response:
        return Response([
            game_mode.repr()
            for game_mode in GameMode.objects.filter(active=True)
        ])
