from dataclasses import field

import order_details
from cartproducts.models import Cartproducts
from carts.models import Cart
from order_details.models import OrderDetails
from rest_framework import serializers
from rest_framework.exceptions import APIException

from .models import Order


class QuantityOrderError(APIException):
    status_code = 400


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
        read_only_fields = ["id", "user", "order_total"]

    def create(self, validated_data: dict):

        user_id = self.context.get("view").kwargs.get("user_id")
        user_cart = Cart.objects.get(user_id=user_id)

        user_cart_products = Cartproducts.objects.filter(cart_id=user_cart.id)

        # verificando se a quantidade de produtos no estoque é suficiente

        products_not_enough = {}

        for cart_product in user_cart_products:
            products_in_cart = cart_product.quantity_in_cart
            products_in_inventory = cart_product.product.quantity
            product_name = cart_product.product.name
            product_id = cart_product.product.id

            if products_in_cart > products_in_inventory:
                products_not_enough.update(
                    {
                        product_id: f"The product {product_name} has {products_in_inventory} in inventory. You ordered {products_in_cart}."
                    }
                )

        if products_not_enough:
            raise QuantityOrderError(products_not_enough)

        # criar ordem

        order = Order.objects.create(user_id=user_id, order_total=user_cart.subtotal)

        # criar e preencher order details

        for cart_product in user_cart_products:
            product_id = cart_product.product.id
            products_in_order = cart_product.quantity_in_cart
            order_id = order.id

            price = cart_product.product.price
            discount = cart_product.product.product_discount.discount_percent

            final_price = price * discount

            order_details = OrderDetails.objects.create(
                final_price=final_price,
                quantity_in_order=products_in_order,
                order_id=order_id,
                product_id=product_id,
            )

            # limpar cart products
            cart_product.delete()

        user_cart.subtotal = 0

        user_cart.save()

        return order
