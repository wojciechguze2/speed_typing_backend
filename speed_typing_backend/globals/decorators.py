import os
import traceback

from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from rest_framework import status
from sentry_sdk import capture_exception


def exception_decorator():
    def decorator(func):
        def inner(request, *args, **kwargs):
            try:
                return func(request, *args, **kwargs)
            except Exception as e:
                if os.getenv('SENTRY_DSN'):
                    capture_exception(e)
                elif os.getenv('LOCAL_DEBUG'):
                    traceback.print_exc()

                if hasattr(e, 'http_status'):
                    http_status = e.http_status
                elif hasattr(e, 'status_code'):
                    http_status = e.status_code
                elif isinstance(e, ObjectDoesNotExist):
                    http_status = 404
                else:
                    http_status = status.HTTP_500_INTERNAL_SERVER_ERROR

                return JsonResponse(
                    {
                        'reason': 'Exception',
                        'detail': repr(e),
                    },
                    safe=False,
                    status=http_status
                )

        return inner

    return decorator
