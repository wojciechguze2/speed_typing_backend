from django.urls import path
from .views import *

translation = TranslationViewSet.as_view({
    'get': 'retrieve',
    'patch': 'update',
    'delete': 'delete',
})

translations = TranslationsViewSet.as_view({
    'post': 'create',
})

locale_translations = TranslationsViewSet.as_view({
    'get': 'list',
})

urlpatterns = [
    path('translations', translations),
    path('translation/<int:translation_id>', translation),
    path('translations/<slug:locale_iso>', locale_translations)
]
