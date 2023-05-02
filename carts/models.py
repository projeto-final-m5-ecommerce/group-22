from django.db import models


class Cart(models.Model):
    quantity = models.IntegerField()
    price = models.FloatField()

    product = models.ManyToManyField(
        "products.Product",
        related_name="Products_Orders",
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

# Será necessário desenvolver uma model para armazenar os produtos que o usuário selecionou, antes de finalizar a compra.
# Deve conter a lista dos produtos que foram pedidos, com o valor nos items.
# Um pedido não pode ser finalizado se não tiver estoque.
# Se os produtos do carrinho forem de diferentes vendedores, deve ser criado um pedido para cada.
