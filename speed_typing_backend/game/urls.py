from django.urls import path
from .views import *

save_game = SaveGameViewSet.as_view({
    'post': 'save'
})

urlpatterns = [
    path('game/save', save_game)
]
