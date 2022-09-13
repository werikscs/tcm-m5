from rest_framework import serializers
import ipdb
from .models import Cartproducts
from products.serializers import ProductSerializer

class CartProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartproducts
        fields = "__all__"
        
        
class ListCartProductsSerializer(serializers.ModelSerializer):
    # product = ProductSerializer(read_only=True)
    class Meta:
        model = Cartproducts
        fields = ['id',"product","quantity", "productValue"]

