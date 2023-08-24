from django.urls import path
from .views import *

translations_cms = TranslationsCmsViewSet.as_view({
    'get': 'list'
})

translation_create_cms = TranslationsCmsViewSet.as_view({
    'get': 'create',
    'post': 'create'
})

translation_update_cms = TranslationsCmsViewSet.as_view({
    'get': 'update',
    'post': 'update'
})

translation_delete_cms = TranslationsCmsViewSet.as_view({
    'get': 'delete'
})

urlpatterns = [
    path('translations', translations_cms, name='cms_translations'),
    path('translations/create', translation_create_cms, name='cms_create_translation'),
    path('translations/<int:translation_base_id>', translation_update_cms, name='cms_update_translation'),
    path('translations/<int:translation_base_id>/delete', translation_delete_cms, name='cms_delete_translation'),
]
