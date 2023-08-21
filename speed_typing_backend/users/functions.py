from django.contrib.auth.models import User
from rest_framework.request import Request
from rest_framework_jwt.serializers import jwt_decode_handler


def request_user(request: Request):
    token = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[1]
    decoded_token = jwt_decode_handler(token)

    user_id = decoded_token['user_id']

    return User.objects.get(id=user_id)
