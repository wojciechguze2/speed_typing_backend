from django.template.response import TemplateResponse
from rest_framework.request import Request

from cms.security.views import BaseCmsViewSet
from speed_typing_backend.globals.decorators import exception_decorator


class CmsViewSet(BaseCmsViewSet):
    @staticmethod
    @exception_decorator()
    def retrieve(request: Request):
        template_name = 'cms/homepage/index.html'

        return TemplateResponse({}, template_name)
