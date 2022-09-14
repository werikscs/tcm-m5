import ipdb
from carts.models import Cart
from discounts.models import Discount
from products.serializers import ProductSerializer
from rest_framework import serializers

from .models import Cartproducts


class CartProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartproducts
        fields = "__all__"

    def create(self, validated_data):

        cart = validated_data.get("cart")
        product = validated_data.get("product")
        quantity_to_cart = validated_data.get("quantity")

        cartproduct_obj = Cartproducts.objects.filter(cart_id=cart, product_id=product)

        quantity_to_subtotal = 0

        if cartproduct_obj:
            if quantity_to_cart:
                cartproduct_obj.quantity += quantity_to_cart
                quantity_to_subtotal = quantity_to_cart

            else:
                cartproduct_obj.quantity += 1
                quantity_to_subtotal = 1

            cartproduct_obj.save()

        else:
            cartproduct_obj = Cartproducts.objects.create(**validated_data)
            quantity_to_subtotal = quantity_to_cart or 1

        cart_obj = Cart.objects.get(id=cart.id)

        discount_id = cartproduct_obj.product.discount_id
        discount_obj = Discount.objects.get(id=discount_id)

        product_price = cartproduct_obj.product.price
        discount = discount_obj.discount_percent

        cart_obj.subtotal += product_price * discount * quantity_to_subtotal
        cart_obj.save()

        return cartproduct_obj


class ListCartProductsSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Cartproducts
        fields = ["id", "product", "quantity"]
