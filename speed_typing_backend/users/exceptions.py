from rest_framework import status


class UsersLimitReached(Exception): ...


class UserAlreadyExists(Exception):
    def __init__(self):
        self.http_status = status.HTTP_409_CONFLICT
        super(UserAlreadyExists, self).__init__('User already exists.')
