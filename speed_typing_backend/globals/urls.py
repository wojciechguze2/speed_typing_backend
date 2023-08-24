from django.urls import path
from .views import *

game_modes_global_data = GameModesDataViewSet.as_view({
    'get': 'retrieve',
})

static_page = StaticPageViewSet.as_view({
    'get': 'retrieve',
})

contact = ContactViewSet.as_view({
    'post': 'send',
})

urlpatterns = [
    path('globals/game-modes-data', game_modes_global_data),
    path('globals/static-page/<slug:static_page_path>', static_page),
    path('globals/contact', contact),
]
