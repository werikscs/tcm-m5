from rest_framework import permissions

class GetOrIsStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        #verifica se a requisição é do tipo get
        if request.method in permissions.SAFE_METHODS:
            return True

        return (
          request.user.is_authenticated
          and request.user.is_staff or request.user.is_superuser
          )