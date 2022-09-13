from django.db import models
from jsonfield import JSONField

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_id = models.PositiveIntegerField(default=1)
    category_id = JSONField()

    product_category = models.ManyToManyField("categories.Category", related_name="products")
    product_discount = models.ForeignKey("discounts.Discount", on_delete=models.CASCADE, related_name="products")