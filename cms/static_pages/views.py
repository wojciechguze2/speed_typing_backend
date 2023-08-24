from django.template.response import TemplateResponse
from rest_framework.request import Request

from cms.security.views import BaseCmsViewSet
from speed_typing_backend.globals.decorators import exception_decorator
from speed_typing_backend.globals.models import StaticPage


class StaticPagesCmsViewSet(BaseCmsViewSet):
    template_name = 'cms/static_pages/index.html'

    @staticmethod
    @exception_decorator()
    def list(request: Request):
        template_name = 'cms/static_pages/index.html'

        return TemplateResponse(
            request,
            template_name,
            context={
                'staticPages': [
                    static_page.repr()
                    for static_page in StaticPage.objects.all()
                ]
            }
        )
