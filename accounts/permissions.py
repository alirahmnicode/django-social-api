from rest_framework import permissions


class UpdateOwnAccount(permissions.BasePermission):
    """Allow user to edit their own account"""

    def has_object_permission(self, request, view, obj):
        """Check user is tryin to edit their own account"""
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id