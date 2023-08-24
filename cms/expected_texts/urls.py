from django.urls import path
from .views import *

expected_texts_cms = ExpectedTextsCmsViewSet.as_view({
    'get': 'list'
})


urlpatterns = [
    path('expected-texts', expected_texts_cms, name='cms_expected_texts'),
]
