from django.db import models

# Create your models here.
class Discount(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    discount_percent = models.DecimalField(decimal_places=3, max_digits=4)