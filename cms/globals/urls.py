from django.urls import path

from cms.globals.views import CmsViewSet

cms_homepage = CmsViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    path('', cms_homepage, name='cms_homepage'),
]
