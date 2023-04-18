from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from accounts.models import CustomUser
from accounts.serializers import UserSerializer
from accounts.permissions import UpdateOwnAccount


class UserViewSet(viewsets.ModelViewSet):
    """Handle creating and updating users"""
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnAccount,)