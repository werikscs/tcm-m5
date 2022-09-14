from django.db import models


class Cart(models.Model):
    subtotal = models.DecimalField(default=0, max_digits=10, decimal_places=2)

    user = models.OneToOneField(
        "users.User", on_delete=models.CASCADE, related_name="cart"
    )
