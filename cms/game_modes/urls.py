from django.urls import path
from .views import *

game_modes_cms = GameModesCmsViewSet.as_view({
    'get': 'list'
})

urlpatterns = [
    path('game-modes', game_modes_cms, name='cms_game_modes'),
]
