from django.db import models


class Cart(models.Model):
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    user = models.OneToOneField(
        "users.User", on_delete=models.CASCADE, related_name="cart"
    )

    cart_products = models.ManyToManyField(
        "products.Product",
        through="ProductsCart",
        related_name="carts",
    )


class ProductsCart(models.Model):
    product = models.ForeignKey(
        "products.Product",
        on_delete=models.RESTRICT,
    )
    cart = models.ForeignKey(
        "carts.Cart",
        on_delete=models.RESTRICT,
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=1)
