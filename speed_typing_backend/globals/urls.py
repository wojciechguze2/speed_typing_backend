from django.urls import path
from .views import *

game_modes_global_data = GameModesDataViewSet.as_view({
    'get': 'retrieve',
})

urlpatterns = [
    path('globals/game-modes-data', game_modes_global_data),
]
