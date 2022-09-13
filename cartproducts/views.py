from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView, Request, Response, status
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from carts.models import Cart
from discounts.models import Discount
from products.models import Product

import ipdb


# from .mixins import SerializerByMethodMixin
from .models import Cartproducts
# from .permissions import IsAdminOrOwner, IsAdminToGet

from .serializers import CartProductsSerializer

class CartProductsView(generics.CreateAPIView):
    queryset = Cartproducts.objects.all()
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [GetOrIsStaff]
    serializer_class = CartProductsSerializer

    def perform_create(self, serializer):
        
        product_obj = get_object_or_404(Product, id=self.request.data["product"])
        cart_obj = get_object_or_404(Cart, id=self.request.data["cart"])        
        discount_obj = get_object_or_404(Discount, id=product_obj.discount_id)
        
        serializer.save(productValue=product_obj.price*discount_obj.discount_percent)
    