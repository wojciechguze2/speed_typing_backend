from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework_jwt.serializers import RefreshJSONWebTokenSerializer
from rest_framework_jwt.settings import api_settings
from speed_typing_backend.globals.decorators import exception_decorator
from speed_typing_backend.users.exceptions import UsersLimitReached, UserAlreadyExists
from speed_typing_backend.users.functions import request_user


class LoginViewSet(ViewSet):
    @staticmethod
    @exception_decorator()
    def login(request: Request) -> Response:
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(username=email, password=password)

        if user:
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)

            return Response({'token': token})

        return Response(status=status.HTTP_401_UNAUTHORIZED)


class RegisterViewSet(ViewSet):
    @staticmethod
    @exception_decorator()
    def register(request: Request) -> Response:
        if User.objects.count() > settings.USERS_LIMIT:
            raise UsersLimitReached

        try:
            User.objects.create_user(
                username=request.data['email'],
                email=request.data['email'],
                password=request.data['password']
            )
        except IntegrityError:
            raise UserAlreadyExists

        return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)


class TokenViewSet(ViewSet):
    permission_classes = (IsAuthenticated, )

    @staticmethod
    @exception_decorator()
    def refresh(request: Request) -> Response:
        serializer = RefreshJSONWebTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data['token']

        return Response({'token': token})


class UserViewSet(ViewSet):
    permission_classes = (IsAuthenticated, )

    @staticmethod
    @exception_decorator()
    def retrieve(request: Request) -> Response:
        user = request_user(request)

        user_games = user.usergame_set

        if user_games.exists():
            last_game_mode = user_games.order_by('-create_date').first().game_mode.code
        else:
            last_game_mode = '-'

        return Response({
            'email': user.email,
            'lastLoginDate': user.last_login.strftime('%Y-%m-%d %H:%M:%S') if user.last_login else '-',
            'createDate': user.date_joined.strftime('%Y-%m-%d %H:%M:%S') if user.date_joined else '-',
            'lastGameModeCode': last_game_mode
        })


class UserStatisticsViewSet(ViewSet):
    permission_classes = (IsAuthenticated, )

    @staticmethod
    @exception_decorator()
    def retrieve(request: Request) -> Response:
        user = request_user(request)

        user_games = user.usergame_set.all()
        user_statistics = user.userstatistics if hasattr(user, 'userstatistics') else None

        return Response({

        })


class UserGamesHistoryViewSet(ViewSet):
    permission_classes = (IsAuthenticated, )

    @staticmethod
    @exception_decorator()
    def retrieve(request: Request) -> Response:
        user = request_user(request)

        return Response([
            user_game.repr()
            for user_game in user.usergame_set.all()
        ])
