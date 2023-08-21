from rest_framework import status


class ExpectedTextAlreadyExists(Exception):
    def __init__(self):
        self.http_status = status.HTTP_409_CONFLICT
        super(ExpectedTextAlreadyExists, self).__init__('Expected text already exists.')
