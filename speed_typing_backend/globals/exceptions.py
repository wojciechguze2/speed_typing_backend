from rest_framework import status


class ObjectAlreadyExists(Exception):
    def __init__(self):
        self.http_status = status.HTTP_409_CONFLICT
        super(ObjectAlreadyExists, self).__init__('Object already exists.')
