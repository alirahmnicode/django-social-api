from rest_framework import serializers

from accounts.serializers import UserSerializer
from .models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("id", "author_name", "content", "created_at")


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    user = UserSerializer(required=False)

    class Meta:
        model = Post
        fields = ("id", "title", "content", "image", "user", "created_at", "comments")

    def create(self, validated_data):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user

        post = Post.objects.create(
            title=validated_data.get("title"),
            content=validated_data.get("content"),
            user=user,
            image=validated_data.get("image"),
        )
        return post

