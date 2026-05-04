from rest_framework.permissions import BasePermission
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        # allow safe methods
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user

class IsAuthorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET']:
            return True
        return request.user.role == 'author' or request.user.role == 'admin'

    def has_object_permission(self, request, view, obj):
        if request.method in ['GET']:
            return True
        return obj.author == request.user or request.user.role == 'admin'