from django.db import models


class Cart(models.Model):
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
<<<<<<< HEAD

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="Cart"
=======
    user = models.OneToOneField(
        "users.User", on_delete=models.CASCADE, related_name="cart"
>>>>>>> 21f38fa247731a8bbe45c5295beb9dd5f8625af6
    )

    cart_products = models.ManyToManyField(
        "products.Product",
        related_name="carts",
    )


""" 
class ProductsOrders(models.Model):
    product = models.ForeignKey(
        "products.Product",
        on_delete=models.RESTRICT,
    )
    order = models.ForeignKey(
        "orders.Order",
        on_delete=models.RESTRICT,
    )
 """
