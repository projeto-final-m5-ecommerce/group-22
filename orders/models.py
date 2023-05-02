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


# Associado a cada pedido deve conter seu status PEDIDO REALIZADO, EM ANDAMENTO ou ENTREGUE para acompanhamento do usuário.
# Toda vez que o status do pedido for atualizado deve ser enviado um email ao comprador.
# Deve conter todos os dados dos produtos, menos a quantidade em estoque.
# O vendedor do produto deve conseguir atualizar o status do pedido.
# Deverá conter o horário que o pedido foi feito.
