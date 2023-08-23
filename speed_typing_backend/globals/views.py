from django.db.models import Count
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from speed_typing_backend.game_modes.models import GameMode
from speed_typing_backend.globals.decorators import exception_decorator


class GameModesDataViewSet(ViewSet):
    @staticmethod
    @exception_decorator()
    def retrieve(request: Request):
        global_max_game_modes = int(request.query_params.get('global_max_game_modes', 3))
        active_game_modes = GameMode.objects.filter(
            active=True,
        )

        most_popular_game_modes = active_game_modes.annotate(
            game_count=Count('game')
        ).order_by('-game_count')[:global_max_game_modes]

        new_game_modes = active_game_modes.order_by(
            '-create_date'
        )[:global_max_game_modes]

        return Response({
            'mostPopularGameModes': [
                game_mode.repr()
                for game_mode in most_popular_game_modes
            ],
            'newGameModes': [
                game_mode.repr()
                for game_mode in new_game_modes
            ]
        })
