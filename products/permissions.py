from rest_framework import permissions


class IsAdminOrSeller(permissions.BasePermission):
    def has_permission(self, request, view) -> bool:
        return request.user.is_superuser or request.user.is_seller
