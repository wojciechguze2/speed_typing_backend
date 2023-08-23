from django.urls import path
from .views import *

save_game = SaveGameViewSet.as_view({
    'post': 'save'
})

game_expected_text = GameExpectedTextViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    path('game/save', save_game),
    path('game/expected-text', game_expected_text)
]
