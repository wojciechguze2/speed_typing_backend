from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from speed_typing_backend.authors.models import Author
from speed_typing_backend.constants import DEFAULT_PAGINATION_LIMIT
from speed_typing_backend.expected_texts.exceptions import ExpectedTextAlreadyExists
from speed_typing_backend.expected_texts.models import ExpectedText
from speed_typing_backend.globals.decorators import exception_decorator


class ExpectedTextsViewSet(ViewSet):
    @staticmethod
    @exception_decorator()
    def list(request: Request) -> Response:
        locale_iso = request.query_params.get('locale_iso')
        offset = int(request.query_params.get('offset', 0))
        limit = int(request.query_params.get('limit', DEFAULT_PAGINATION_LIMIT))

        expected_texts = ExpectedText.objects.all()

        if locale_iso:
            expected_texts = expected_texts.filter(locale__iso=locale_iso)

        count = expected_texts.count()
        expected_texts = expected_texts[offset: offset + limit]

        return Response({
            'expectedTexts': [
                expected_text.repr()
                for expected_text in expected_texts
            ],
            'count': count
        })

    @staticmethod
    @exception_decorator()
    def retrieve(request: Request, expected_text_id: int) -> Response:
        expected_text = ExpectedText.objects.get(id=expected_text_id)

        return Response(expected_text.repr())

    @staticmethod
    @exception_decorator()
    def create(request: Request) -> Response:
        text = request.data.get('text').strip()

        if not text:
            raise ValueError

        author_id = request.data.get('authorIdentity')

        expected_text, created = ExpectedText.objects.get_or_create(
            text=text,
            author_id=author_id
        )

        if not created:
            raise ExpectedTextAlreadyExists

        return Response(expected_text.repr())

    @staticmethod
    @exception_decorator()
    def update(request: Request, expected_text_id: int) -> Response:
        return Response(None)  # disabled so it doesn't break history
        expected_text = ExpectedText.objects.get(id=expected_text_id)

        text = request.data.get('text').strip()

        if not text:
            raise ValueError

        author_id = request.data.get('authorIdentity')

        if ExpectedText.objects.filter(text=text, author_id=author_id).exists():
            raise ExpectedTextAlreadyExists

        author = Author.objects.get(id=author_id)

        expected_text.text = text
        expected_text.author_id = author.id
        expected_text.save(update_fields=[
            'text',
            'author_id'
        ])

        return Response(expected_text.repr())

    @staticmethod
    @exception_decorator()
    def delete(request: Request, expected_text_id: int) -> Response:
        expected_text = ExpectedText.objects.filter(id=expected_text_id)

        if expected_text.exists():
            expected_text.active = False
            expected_text.save(update_fields=['active'])

        return Response(None, status=status.HTTP_204_NO_CONTENT)