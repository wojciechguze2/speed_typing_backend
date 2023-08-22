from speed_typing_backend.users.models import CustomUser
from django.core.exceptions import MultipleObjectsReturned
from rest_framework.request import Request
from rest_framework_jwt.serializers import jwt_decode_handler

from speed_typing_backend.users.exceptions import UserIsNotActive


def request_user(request: Request) -> CustomUser:
    token = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[1]
    decoded_token = jwt_decode_handler(token)

    user_id = decoded_token['user_id']

    users = CustomUser.objects.filter(id=user_id, is_active=True)

    if users.exists():
        if users.count() == 1:
            return users.first()

        raise MultipleObjectsReturned
    else:
        if CustomUser.objects.filter(id=user_id).exists():
            raise UserIsNotActive

        raise CustomUser.DoesNotExist
