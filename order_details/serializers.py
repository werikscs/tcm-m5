from rest_framework import serializers

from .models import OrderDetails


class OrderDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetails
        fields = ["id", "product", "quantity_in_order", "final_price"]
