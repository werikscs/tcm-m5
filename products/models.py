from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    category_id = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_id = models.PositiveIntegerField(default=1)

    category = models.ManyToManyField("categories.Category", on_delete=models.CASCADE, related_name="products")
    discount = models.ForeignKey("discounts.Discount", on_delete=models.CASCADE, related_name="products")