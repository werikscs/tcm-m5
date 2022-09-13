from rest_framework import serializers
from cartproducts.serializers import CartProductsSerializer, ListCartProductsSerializer
from .models import Cart


class CartSerializer(serializers.ModelSerializer):
    cartproducts = ListCartProductsSerializer(many=True, read_only=True)
    
    class Meta:
        model = Cart
        fields = [
            'id',
            'subtotal',
            'user',
            'cartproducts'
        ]
        read_only_fields = ['subtotal','user']

