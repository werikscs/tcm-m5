from django.db import models


# Create your models here.
class OrderDetails(models.Model):
    final_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    quantity_in_order = models.PositiveIntegerField(default=0)

    order = models.ForeignKey(
        "orders.Order", on_delete=models.CASCADE, related_name="order_details"
    )
    product = models.ForeignKey(
        "products.Product", on_delete=models.CASCADE, related_name="order_details"
    )
