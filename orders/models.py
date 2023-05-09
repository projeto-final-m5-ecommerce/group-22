from django.db import models


class OrderStatus(models.TextChoices):
    ORDER_PLACED = "Order placed"
    IN_PROGRESS = "In progress"
    DELIVERED = "Delivered"


class Order(models.Model):
    ordered_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=128, choices=OrderStatus.choices, default=OrderStatus.ORDER_PLACED
    )
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="orders"
    )
