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
        


        serializer.save()
    
class CartProductsDetailView(generics.DestroyAPIView):
     queryset = Cartproducts.objects.all()
     serializer_class = CartProductsSerializer
     lookup_url_kwarg = 'cartproduct_id'

     def perform_destroy(self, instance):
        
        qtd_remove = self.request.data.get('quantity')
        discount_obj = Discount.objects.get(id=instance.product.discount_id)
        subtotal = 0
        if qtd_remove and instance.quantity > qtd_remove:
            instance.quantity -= qtd_remove
            subtotal = instance.product.price*discount_obj.discount_percent*qtd_remove
            instance.save()            
        else:           
            subtotal = instance.product.price*discount_obj.discount_percent*instance.quantity    
            instance.delete()

        cart_obj = Cart.objects.get(id=instance.cart.id)
        cart_obj.subtotal -= subtotal
        cart_obj.save()   
     