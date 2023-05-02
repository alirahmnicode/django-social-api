from rest_framework import viewsets
from rest_framework import filters
from rest_framework.permissions import AllowAny, IsAuthenticated

from accounts.models import CustomUser, Profile
from accounts import serializers
from custom_permission.permissions import OwnObject


class UserViewSet(viewsets.ModelViewSet):
    """Handle creating and updating users"""

    serializer_class = serializers.UserSerializer
    queryset = CustomUser.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ("username", "email")

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ["retrieve", "destroy", "update", "partial_update"]:
            permission_classes = [IsAuthenticated, OwnObject]
        elif self.action == "create":
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action in ["retrieve", "destroy", "update", "partial_update"]:
            # return user email field
            self.serializer_class = serializers.UserOwnAccountSerializer
        elif self.action == "create":
            # use UserRegisterationSerializer for return token
            self.serializer_class = serializers.UserRegisterationSerializer
        else:
            # only username field
            self.serializer_class = serializers.UserSerializer
        return super().get_serializer_class()


class ProfileViewSet(viewsets.ModelViewSet):
    """Handle CURD profile"""

    serializer_class = serializers.ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_permissions(self):
        """set own account permision for unsafe methods"""
        permission_classes = [IsAuthenticated]

        if self.action in ["create", "update", "destroy", "partial_update"]:
            permission_classes = [IsAuthenticated, OwnObject]

        return [permission() for permission in permission_classes]
