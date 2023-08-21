from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from speed_typing_backend.expected_texts.models import ExpectedText
from speed_typing_backend.globals.decorators import exception_decorator


class ExpectedTextsViewSet(ViewSet):
    @staticmethod
    @exception_decorator()
    def list(request: Request) -> Response:
        return Response([
            expected_text.repr()
            for expected_text in ExpectedText.objects.all()
        ])

    @staticmethod
    @exception_decorator()
    def retrieve(request: Request, expected_text_id: int) -> Response:
        expected_text = ExpectedText.objects.get(id=expected_text_id)

        return Response(expected_text.repr())
