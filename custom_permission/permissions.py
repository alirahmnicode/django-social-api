from rest_framework.permissions import BasePermission


class OwnObject(BasePermission):
    """Check if the object is for the current user"""
    def has_object_permission(self, request, view, obj):
        return obj.user.id == request.user.id
