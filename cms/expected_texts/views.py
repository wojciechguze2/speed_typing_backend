from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from django.urls import reverse
from rest_framework.request import Request

from cms.expected_texts.forms import ExpectedTextForm
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

    @staticmethod
    @exception_decorator()
    def create(request: Request) -> [TemplateResponse, HttpResponseRedirect]:
        template_name = 'cms/expected_texts/create.html'

        if request.method == 'POST':
            form = ExpectedTextForm(request.POST)

            if form.is_valid():
                form.save()

                return HttpResponseRedirect(reverse('cms_expected_texts'))
        else:
            form = ExpectedTextForm()

        return TemplateResponse(
            request,
            template_name,
            context={
                'form': form,
            }
        )

    @staticmethod
    @exception_decorator()
    def update(request: Request, expected_text_id: int) -> [TemplateResponse, HttpResponseRedirect]:
        template_name = 'cms/expected_texts/update.html'

        expected_text = get_object_or_404(ExpectedText, id=expected_text_id)

        if request.method == 'POST':
            form = ExpectedTextForm(request.POST, instance=expected_text)

            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('cms_expected_texts'))
        else:
            form = ExpectedTextForm(instance=expected_text)

        return TemplateResponse(
            request,
            template_name,
            context={
                'expectedText': expected_text_id,
                'form': form
            }
        )

    @staticmethod
    @exception_decorator()
    def delete(request: Request, expected_text_id: int) -> HttpResponseRedirect:
        ExpectedText.objects.get(id=expected_text_id).delete()

        return HttpResponseRedirect(reverse('cms_expected_texts'))
