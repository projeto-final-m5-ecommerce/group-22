from django.db import models


class Cart(models.Model):
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="carts"
    )
    cart_products = models.ManyToManyField(
        "products.Product",
        related_name="carts",
    )
