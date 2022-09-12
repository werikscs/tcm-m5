from rest_framework import serializers
from .models import Product
from categories.models import Category
from discounts.models import Discount
from discounts.serializers import DiscountSerializer
from categories.serializers import CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    discount = DiscountSerializer(read_only=True)

    class Meta:
        model = Product
        fields ="__all__"
        