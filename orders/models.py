from django.db import models


class OrderStatus(models.TextChoices):
    ORDER_PLACED = "Order placed"
    IN_PROGRESS = "In progress"
    DELIVERED = "Delivered"


class Order(models.Model):
    ordered_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=128,
        choices=OrderStatus.choices,
        default=OrderStatus.ORDER_PLACED,
    )

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="orders"
    )

    products_orders = models.ManyToManyField(
        "products.Product", through="ProductsOrders", related_name="orders"
    )


class ProductsOrders(models.Model):
    product = models.ForeignKey(
        "products.Product",
        on_delete=models.RESTRICT,
    )
    order = models.ForeignKey(
        "orders.Order",
        on_delete=models.RESTRICT,
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=1)
