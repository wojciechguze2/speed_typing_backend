from django.template.response import TemplateResponse
from rest_framework.request import Request

from cms.security.views import BaseCmsViewSet
from speed_typing_backend.expected_texts.models import ExpectedText
from speed_typing_backend.globals.decorators import exception_decorator


class ExpectedTextsCmsViewSet(BaseCmsViewSet):
    @staticmethod
    @exception_decorator()
    def list(request: Request):
        template_name = 'cms/expected_texts/index.html'

        return TemplateResponse(
            request,
            template_name,
            context={
                'expectedTexts': [
                    expected_text.repr()
                    for expected_text in ExpectedText.objects.all()
                ]
            }
        )
