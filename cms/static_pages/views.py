from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from django.urls import reverse
from rest_framework.request import Request

from cms.security.views import BaseCmsViewSet
from cms.static_pages.forms import StaticPageForm
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

    @staticmethod
    @exception_decorator()
    def create(request: Request) -> [TemplateResponse, HttpResponseRedirect]:
        template_name = 'cms/static_pages/create.html'

        if request.method == 'POST':
            form = StaticPageForm(request.POST)

            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('cms_static_pages'))
        else:
            form = StaticPageForm()

        return TemplateResponse(
            request,
            template_name,
            context={
                'form': form,
            }
        )

    @staticmethod
    @exception_decorator()
    def update(request: Request, static_page_id: int) -> [TemplateResponse, HttpResponseRedirect]:
        template_name = 'cms/static_pages/update.html'

        static_page = get_object_or_404(StaticPage, id=static_page_id)

        if request.method == 'POST':
            form = StaticPageForm(request.POST, instance=static_page)

            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('cms_static_pages'))
        else:
            form = StaticPageForm(instance=static_page)

        return TemplateResponse(
            request,
            template_name,
            context={
                'staticPage': static_page,
                'form': form
            }
        )

    @staticmethod
    @exception_decorator()
    def delete(request: Request, static_page_id: int) -> HttpResponseRedirect:
        StaticPage.objects.get(id=static_page_id).delete()

        return HttpResponseRedirect(reverse('cms_static_pages'))
