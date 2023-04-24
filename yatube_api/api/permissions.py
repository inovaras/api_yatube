from rest_framework import permissions
# разрешить только аут-нным ->  чтение
# разрешить только автор ->  has_object_permissions


class AuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request,
                       view):
        return (
                request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class UserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request,
                       view):
        return (
                request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user