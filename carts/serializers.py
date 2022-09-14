from cartproducts.models import Cartproducts
from cartproducts.serializers import ListCartProductsSerializer
from rest_framework import serializers

from .models import Cart


class CartSerializer(serializers.ModelSerializer):
    cartproducts = ListCartProductsSerializer(many=True, read_only=True)
    subtotal = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ["id", "subtotal", "user", "cartproducts"]
        read_only_fields = ["subtotal", "user"]

    def get_subtotal(self, cart: Cart):

        cart_products = Cartproducts.objects.filter(cart_id=cart.id)

        subtotal = 0

        for item in cart_products:
            product = item.product

            price = product.price
            discount = product.product_discount.discount_percent
            quantity = item.quantity_in_cart

            subtotal += price * discount * quantity

        return subtotal
