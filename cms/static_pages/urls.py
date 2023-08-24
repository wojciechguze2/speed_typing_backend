from django.urls import path
from .views import *

static_pages_cms = StaticPagesCmsViewSet.as_view({
    'get': 'list'
})

urlpatterns = [
    path('static-pages', static_pages_cms, name='cms_static_pages'),
]
