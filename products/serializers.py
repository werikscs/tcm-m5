from rest_framework import serializers
from .models import Product
from categories.models import Category
from discounts.models import Discount
from discounts.serializers import DiscountSerializer
from categories.serializers import CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    product_category = CategorySerializer(read_only=True)
    product_discount = DiscountSerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True, default=1)
    discount_id = serializers.IntegerField(write_only=True, default=1)

    class Meta:
        model = Product
        fields ="__all__"
