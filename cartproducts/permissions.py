from rest_framework import permissions
from rest_framework.views import Request, View
from .models import Cartproducts
import ipdb
from carts.models import Cart

class IsOwnerOrAdminOrStaff(permissions.BasePermission):
    
    def has_object_permission(
        self,
        request: Request,
        view: View,
        cartProducts: Cartproducts,
    ) -> bool:
        
        
        return cartProducts.cart.user == request.user or request.user.is_superuser or request.user.is_staff

class isOwnerAdminStaff(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:   
        cart_obj = Cart.objects.get(id=request.data['cart'])        

        return cart_obj.user == request.user or request.user.is_superuser or request.user.is_staff
        