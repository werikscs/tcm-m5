from rest_framework import serializers
import ipdb
from .models import Wishlist
from products.serializers import ProductSerializer
from django.shortcuts import get_object_or_404
from rest_framework.validators import UniqueValidator
from rest_framework.exceptions import APIException

from products.models import Product
from users.models import User

class UniqueValidationError(APIException):
    status_code = 403

class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = "__all__"
        read_only_fields = ['user']

    def validate_product(self, value: int):
        userid= self.context['view'].kwargs['user_id']
        if Wishlist.objects.filter(product_id= value, user_id=userid).exists():
            raise UniqueValidationError("product already added to wishlist")

        return value

class WishlistGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = "__all__"
        read_only_fields = ['user']

    product = ProductSerializer(read_only=True)



    
        