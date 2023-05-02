from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment
from custom_permission.permissions import OwnObject


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        if self.action in ["update", "destroy", "partial_update"]:
            permission_classes = [IsAuthenticated, OwnObject]
        return [permission() for permission in permission_classes]
