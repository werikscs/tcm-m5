from carts.models import Cart
from rest_framework import permissions
from rest_framework.views import Request, Response, View, status

from .models import Cartproducts


class IsOwnerOrAdminOrStaff(permissions.BasePermission):
    def has_object_permission(
        self,
        request: Request,
        view: View,
        cartProducts: Cartproducts,
    ) -> bool:

        return (
            cartProducts.cart.user == request.user
            or request.user.is_superuser
            or request.user.is_staff
        )


class isOwnerAdminStaff(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        return request.user.is_authenticated
