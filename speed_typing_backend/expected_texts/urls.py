from django.urls import path
from .views import *

expected_texts = ExpectedTextsViewSet.as_view({
    'get': 'list',
    'post': 'create',
    'patch': 'update'
})

expected_text = ExpectedTextsViewSet.as_view({
    'get': 'retrieve'
})

random_expected_text = ExpectedTextsViewSet.as_view({
    'get': 'random'
})

urlpatterns = [
    path('expected-texts', expected_texts),
    path('expected-texts/<int:expected_text_id>', expected_text),
    path('expected-texts/random', random_expected_text),
]
