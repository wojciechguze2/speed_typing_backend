from django.urls import path
from .views import *

login_cms = LoginCmsViewSet.as_view()

logout_cms = LogoutCmsViewSet.as_view()

urlpatterns = [
    path('login', login_cms, name='cms_login'),
    path('logout', logout_cms, name='cms_logout'),
]
