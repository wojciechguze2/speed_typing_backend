from django.urls import path
from .views import *

login = LoginViewSet.as_view({
    'post': 'login'
})

register = RegisterViewSet.as_view({
    'post': 'register'
})

token_refresh = TokenViewSet.as_view({
    'post': 'refresh'
})

user = UserViewSet.as_view({
    'get': 'retrieve',
    'patch': 'update',
    'delete': 'delete'
})

user_statistics = UserStatisticsViewSet.as_view({
    'get': 'retrieve'
})

user_history = UserGamesHistoryViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    path('user', user),
    path('user/statistics', user_statistics),
    path('user/history', user_history),
    path('users/login', login, name='login'),
    path('users/register', register, name='register'),
    path('users/token/refresh', token_refresh, name='token_refresh'),
]
