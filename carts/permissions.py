from rest_framework import permissions
from rest_framework.views import Request, View
from .models import Cart
import ipdb

class IsUserOwnerOrAdminOrStaff(permissions.BasePermission):
   

    def has_object_permission(
        self,
        request: Request,
        view: View,
        cart: Cart,
    ) -> bool:
        
        
        return cart.user == request.user or request.user.is_superuser or request.user.is_staff
        