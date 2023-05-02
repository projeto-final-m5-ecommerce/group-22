from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    available = models.BooleanField(default=True)

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="products"
    )


# O usuário deve ter acesso a uma rota onde pode buscar os produtos por nome, categoria e id.
# Deverá ter um estoque dos itens, quando o item estiver com 0 unidades deverá ter um campo indicando que o produto está indisponível.
# Caso um usuário tenha um produto no carrinho e ao finalizar a compra este produto estiver indisponível deve retornar um erro indicando que o produto não está mais disponível.
# Ao ser criado um pedido, deve subtrair a quantidade dos produtos do estoque.
