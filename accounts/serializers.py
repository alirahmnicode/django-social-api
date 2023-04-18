from rest_framework import serializers

from accounts import models


class UserSerializer(serializers.ModelSerializer):
    """Serializes a user object"""

    class Meta:
        model = models.CustomUser
        fields = ("id", "username", "email", "password")
        extra_kwargs = {
            "password": {
                "write_only": True,
                "style": {"input_type": "password"}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.CustomUser.objects.create_user(
            username = validated_data.get("username"),
            email = validated_data.get("email"),
            password = validated_data.get("password")
        )
        return user
    