from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from accounts import models


class UserRegisterationSerializer(serializers.ModelSerializer):
    """Serializes a user object only for authentication"""

    token = serializers.SerializerMethodField("get_token")

    class Meta:
        model = models.CustomUser
        fields = ("id", "username", "email", "password", "token")
        extra_kwargs = {
            "password": {"write_only": True, "style": {"input_type": "password"}}
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.CustomUser.objects.create_user(
            username=validated_data.get("username"),
            email=validated_data.get("email"),
            password=validated_data.get("password"),
        )
        return user

    def get_token(self, user):
        """Return token in response"""
        data = dict()
        # get token data
        refresh = RefreshToken.for_user(user)

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)

        return data


class UserOwnAccountSerializer(serializers.ModelSerializer):
    """user this serializer for access user to own account fields"""

    class Meta:
        model = models.CustomUser
        fields = ("id", "username", "email", "password")
        extra_kwargs = {
            "password": {"write_only": True, "style": {"input_type": "password"}},
        }


class UserSerializer(serializers.ModelSerializer):
    """Serializes a user object"""

    class Meta:
        model = models.CustomUser
        fields = ("id", "username")


class ProfileSerializer(serializers.ModelSerializer):
    """Serializes a profile object"""

    following = UserSerializer(many=True, read_only=True)
    followers = UserSerializer(many=True, read_only=True)

    class Meta:
        model = models.Profile
        fields = (
            "id",
            "first_name",
            "last_name",
            "avatar",
            "following",
            "followers",
            "created_at",
        )
        extra_kwargs = {"avatar": {"required": False}}
        read_only_fields = ["id", "following", "followers", "created_at"]
