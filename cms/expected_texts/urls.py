from django.urls import path
from .views import *

expected_texts_cms = ExpectedTextsCmsViewSet.as_view({
    'get': 'list'
})

expected_text_create_cms = ExpectedTextsCmsViewSet.as_view({
    'get': 'create',
    'post': 'create'
})

expected_text_update_cms = ExpectedTextsCmsViewSet.as_view({
    'get': 'update',
    'post': 'update'
})

expected_text_delete_cms = ExpectedTextsCmsViewSet.as_view({
    'get': 'delete'
})

urlpatterns = [
    path('expected-texts', expected_texts_cms, name='cms_expected_texts'),
    path('expected-texts/create', expected_text_create_cms, name='cms_create_expected_text'),
    path('expected-texts/<int:expected_text_id>', expected_text_update_cms, name='cms_update_expected_text'),
    path('expected-texts/<int:expected_text_id>/delete', expected_text_delete_cms, name='cms_delete_expected_text'),
]
