from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth import get_user_model

from django.contrib.auth.views import LoginView, LogoutView
from rest_framework.viewsets import ViewSet

User = get_user_model()


class BaseCmsViewSet(ViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]


class LoginCmsViewSet(LoginView):
    template_name = 'cms/security/login.html'


class LogoutCmsViewSet(LogoutView):
    template_name = 'cms/security/logout.html'
