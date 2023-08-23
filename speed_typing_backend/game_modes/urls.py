from django.urls import path

from speed_typing_backend.game_modes.views import GameModesViewSet

game_modes = GameModesViewSet.as_view({
    'get': 'list'
})

urlpatterns = [
    path('game-modes', game_modes)
]
