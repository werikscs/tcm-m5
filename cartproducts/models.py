from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Cartproducts(models.Model):
    quantity_in_cart = models.PositiveIntegerField(
        validators=[MinValueValidator(1)], default=1
    )

    cart = models.ForeignKey(
        "carts.Cart", on_delete=models.CASCADE, related_name="cartproducts"
    )
    product = models.ForeignKey(
        "products.Product", on_delete=models.CASCADE, related_name="cartproducts"
    )
