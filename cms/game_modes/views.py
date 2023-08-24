from django.template.response import TemplateResponse
from rest_framework.request import Request

from cms.security.views import BaseCmsViewSet
from speed_typing_backend.game_modes.models import GameMode
from speed_typing_backend.globals.decorators import exception_decorator


class GameModesCmsViewSet(BaseCmsViewSet):
    @staticmethod
    @exception_decorator()
    def list(request: Request):
        template_name = 'cms/game_modes/index.html'

        return TemplateResponse(
            request,
            template_name,
            context={
                'gameModes': [
                    game_mode.repr_long()
                    for game_mode in GameMode.objects.all()
                ]
            }
        )
