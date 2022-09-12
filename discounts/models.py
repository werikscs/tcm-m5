from django.db import models

# Create your models here.
class Discount(models.Model):
    description = models.CharField(max_length=150)
    discount_percent = models.DecimalField(decimal_places=2, max_digits=3)