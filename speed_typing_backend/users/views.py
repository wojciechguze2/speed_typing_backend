from django.conf import settings
from django.contrib.auth import authenticate
from speed_typing_backend.users.models import CustomUser
from django.db import IntegrityError
from django.db.models import Q
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
from speed_typing_backend.users.models import UserStatistics


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
        if CustomUser.objects.count() > settings.USERS_LIMIT:
            raise UsersLimitReached

        try:
            CustomUser.objects.create_user(
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

        user_games = user.game_set

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

    @exception_decorator()
    def update(self, request: Request) -> Response:
        user = request_user(request)
        update_fields = []

        if 'email' in request.data:
            email = request.data.get('email')

            if email != user.email:
                if CustomUser.objects.filter(
                        Q(email=email) | Q(username=email)
                ).exists():
                    raise UserAlreadyExists

                user.email = email
                user.username = email

                update_fields += (
                    'email',
                    'username'
                )

        if 'password' in request.data:
            password = request.data.get('password')

            if not password:
                raise ValueError

            user.set_password(password)
            update_fields.append(
                'password'
            )

        if update_fields:
            user.save(update_fields=update_fields)

        return self.retrieve(request)

    @exception_decorator()
    def delete(self, request: Request) -> Response:
        user = request_user(request)
        user.is_active = False
        user.save(update_fields=['is_active'])

        return Response(True)


class UserStatisticsViewSet(ViewSet):
    permission_classes = (IsAuthenticated, )

    @staticmethod
    @exception_decorator()
    def retrieve(request: Request) -> Response:
        user: CustomUser = request_user(request)
        user_statistics = UserStatistics(user)

        return Response(user_statistics.repr())


class UserGamesHistoryViewSet(ViewSet):
    permission_classes = (IsAuthenticated, )

    @staticmethod
    @exception_decorator()
    def retrieve(request: Request) -> Response:
        user = request_user(request)

        return Response([
            user_game.repr()
            for user_game in user.game_set.all()
        ])
