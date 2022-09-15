import ipdb
from carts.models import Cart
from rest_framework import permissions
from rest_framework.views import Request, View


class IsOwnerOrAdminOrStaff(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        is_auth = request.user.is_authenticated

        if not is_auth:
            return False

        param_id = view.kwargs["user_id"]
        is_admin = request.user.is_superuser
        is_staff = request.user.is_staff
        user_id = request.user.id

        if request.method == "GET":
            return param_id == user_id or is_admin or is_staff

        return param_id == user_id
