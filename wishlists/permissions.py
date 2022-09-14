from rest_framework import permissions
from rest_framework.views import Request, View
import ipdb
from carts.models import Cart

class IsOwnerOrAdminOrStaff(permissions.BasePermission):
    
    def has_permission(self, request: Request, view: View) -> bool:   
       
        param_id = view.kwargs['user_id']
        

        return param_id == request.user.id or request.user.is_superuser or request.user.is_staff