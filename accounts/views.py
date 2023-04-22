from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from accounts.models import CustomUser, Profile
from accounts.serializers import UserSerializer, ProfileSerializer
from accounts.permissions import UpdateOwnAccount


class UserViewSet(viewsets.ModelViewSet):
    """Handle creating and updating users"""
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnAccount,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("username", "email")


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ProfileViewSet(viewsets.ModelViewSet):
    """Handle CURD profile"""
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnAccount,)