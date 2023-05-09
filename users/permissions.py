from rest_framework import permissions
from .models import User
from rest_framework.views import View


class IsAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: User) -> bool:
        return request.user.is_superuser
