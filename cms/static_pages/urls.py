from django.urls import path
from .views import *

static_pages_cms = StaticPagesCmsViewSet.as_view({
    'get': 'list'
})

static_page_create_cms = StaticPagesCmsViewSet.as_view({
    'get': 'create',
    'post': 'create'
})

static_page_update_cms = StaticPagesCmsViewSet.as_view({
    'get': 'update',
    'post': 'update'
})

static_page_delete_cms = StaticPagesCmsViewSet.as_view({
    'get': 'delete'
})

urlpatterns = [
    path('static-pages', static_pages_cms, name='cms_static_pages'),
    path('static-pages/create', static_page_create_cms, name='cms_create_static_page'),
    path('static-pages/<int:static_page_id>', static_page_update_cms, name='cms_update_static_page'),
    path('static-pages/<int:static_page_id>/delete', static_page_delete_cms, name='cms_delete_static_page'),
]
