from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from speed_typing_backend.globals.decorators import exception_decorator
from speed_typing_backend.globals.exceptions import ObjectAlreadyExists
from speed_typing_backend.translations.models import Translation, TranslationBase


class TranslationViewSet(ViewSet):
    @staticmethod
    @exception_decorator()
    def retrieve(request, translation_id: str):
        translation = Translation.objects.get(id=translation_id)

        return Response(translation.repr_long())

    @staticmethod
    @exception_decorator()
    def update(request, translation_id: str):
        translation = Translation.objects.get(id=translation_id)

        translation.translation = request.data.get('translation')
        translation.save(update_fields=['translation'])

        return Response(translation.repr_long())

    @staticmethod
    @exception_decorator()
    def delete(request, translation_id: str):
        translation = Translation.objects.get(id=translation_id)

        translation.delete()

        return Response(None, status=status.HTTP_204_NO_CONTENT)


class TranslationsViewSet(ViewSet):
    @staticmethod
    @exception_decorator()
    def create(request):
        translation_base, _ = TranslationBase.objects.get_or_create(
            code=request.data.get('code')
        )

        translation, created = Translation.objects.get_or_create(
            base=translation_base,
            locale_id=request.data.get('localeId'),
            defaults=dict(
                translation=request.data.get('translation')
            )
        )

        if not created:
            raise ObjectAlreadyExists

        return Response(translation.repr_long())

    @staticmethod
    @exception_decorator()
    def list(request, locale_iso: str):
        return Response(Translation.objects.filter(
            locale__iso=locale_iso
        ).values('base__code', 'translation'))

