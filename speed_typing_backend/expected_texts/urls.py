from django.urls import path
from .views import *

expected_texts = ExpectedTextsViewSet.as_view({
    'get': 'list'
})

expected_text = ExpectedTextsViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    path('expected-texts', expected_texts),
    path('expected-texts/<int:expected_text_id>', expected_text),
]
