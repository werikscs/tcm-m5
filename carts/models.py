from django.db import models

class Cart(models.Model):
    subtotal = models.PositiveIntegerField(default=0)

    user = models.OneToOneField("users.User", on_delete=models.CASCADE, related_name='cart')