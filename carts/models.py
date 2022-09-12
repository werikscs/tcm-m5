from django.db import models

class Cart(models.Model):
    subtotal = models.PositiveIntegerField()

    user = models.OneToOneField("users.User", on_delete=models.CASCADE)