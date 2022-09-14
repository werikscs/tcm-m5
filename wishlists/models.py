
from django.db import models

class Wishlist(models.Model):

    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="wishlist")
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE, related_name="wishlist")