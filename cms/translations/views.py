from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from django.urls import reverse
from rest_framework.request import Request

from cms.security.views import BaseCmsViewSet
from cms.translations.forms import TranslationForm, TranslationBaseForm
from speed_typing_backend.globals.decorators import exception_decorator
from speed_typing_backend.globals.models import Locale
from speed_typing_backend.translations.models import TranslationBase, Translation


class TranslationsCmsViewSet(BaseCmsViewSet):
    @staticmethod
    @exception_decorator()
    def list(request: Request) -> TemplateResponse:
        template_name = 'cms/translations/index.html'

        return TemplateResponse(
            request=request,
            template=template_name,
            context={
                'availableLangaugeCodes': Locale.AVAILABLE_LANGUAGE_CODES,
                'translationBases': [
                    translation_base.repr_long()
                    for translation_base in TranslationBase.objects.all()
                ]
            }
        )

    @staticmethod
    @exception_decorator()
    def create(request: Request) -> [TemplateResponse, HttpResponseRedirect]:
        template_name = 'cms/translations/create.html'

        if request.method == 'POST':
            translation_base_form = TranslationBaseForm(request.POST)
            translation_forms = [
                TranslationForm(
                    request.POST,
                    instance=Translation(locale_id=locale_id),
                    prefix=f"translation_{locale_id}",
                )
                for locale_id in Locale.AVAILABLE_LANGUAGE_IDS
            ]

            if all(translation_form.is_valid() for translation_form in translation_forms) and translation_base_form.is_valid():
                translation_base: TranslationBase = translation_base_form.save()

                for translation_form in translation_forms:
                    translation: Translation = translation_form.save(commit=False)
                    translation.base = translation_base
                    translation.save()

                return HttpResponseRedirect(reverse('cms_translations'))
        else:
            translation_base_form = TranslationBaseForm()
            translation_forms = [
                TranslationForm(
                    prefix=f"translation_{locale_id}",
                    instance=Translation(locale_id=locale_id),
                )
                for locale_id in Locale.AVAILABLE_LANGUAGE_IDS
            ]

        return TemplateResponse(
            request,
            template_name,
            context={
                'translationBaseForm': translation_base_form,
                'translationForms': translation_forms
            }
        )

    @staticmethod
    @exception_decorator()
    def update(request: Request, translation_base_id: int) -> [TemplateResponse, HttpResponseRedirect]:
        template_name = 'cms/translations/update.html'

        translation_base = get_object_or_404(TranslationBase, id=translation_base_id)

        if request.method == 'POST':
            translations = []

            for translation in translation_base.translation_set.all():
                prefix = f"translation_{translation.id}"

                form = TranslationForm(request.POST, instance=translation, prefix=prefix)

                if form.is_valid():
                    form.save()

                translations.append(form)

            if all(form.is_valid() for form in translations):
                return HttpResponseRedirect(reverse('cms_translations'))

        return TemplateResponse(
            request,
            template_name,
            context={
                'translationForms': [
                    TranslationForm(instance=translation, prefix=f"translation_{translation.id}")
                    for translation in translation_base.translation_set.order_by('locale_id')
                ],
                'translationBase': translation_base
            })

    @staticmethod
    @exception_decorator()
    def delete(request: Request, translation_base_id: int) -> HttpResponseRedirect:
        TranslationBase.objects.get(id=translation_base_id).delete()

        return HttpResponseRedirect(reverse('cms_translations'))
