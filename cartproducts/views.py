import ipdb
from carts.models import Cart
from discounts.models import Discount
from django.shortcuts import get_object_or_404
from products.models import Product
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView, Request, Response, status

# from .mixins import SerializerByMethodMixin
from .models import Cartproducts
from .permissions import IsOwnerOrAdminOrStaff, isOwnerAdminStaff
from .serializers import CartProductsSerializer


class CartProductsView(generics.CreateAPIView):
    queryset = Cartproducts.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [isOwnerAdminStaff]
    serializer_class = CartProductsSerializer

    def perform_create(self, serializer):

        get_object_or_404(Product, id=self.request.data.get("product"))
        get_object_or_404(Cart, id=self.request.data.get("cart"))
        serializer.save()


class CartProductsDetailView(generics.DestroyAPIView):
    queryset = Cartproducts.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrAdminOrStaff]
    serializer_class = CartProductsSerializer
    lookup_url_kwarg = "cartproduct_id"

    def perform_destroy(self, instance):

        qtd_remove = self.request.data.get("quantity_in_cart")
        discount_obj = Discount.objects.get(id=instance.product.discount_id)

        subtotal = 0

        if qtd_remove and instance.quantity_in_cart > qtd_remove:
            instance.quantity_in_cart -= qtd_remove
            subtotal = (
                instance.product.price * discount_obj.discount_percent * qtd_remove
            )
            instance.save()
        else:
            subtotal = (
                instance.product.price
                * discount_obj.discount_percent
                * instance.quantity_in_cart
            )
            instance.delete()

        cart_obj = Cart.objects.get(id=instance.cart.id)
        cart_obj.subtotal -= subtotal
        cart_obj.save()
