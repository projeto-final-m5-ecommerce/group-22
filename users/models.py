from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_seller = models.BooleanField(default=False)


# O sistema deve permitir o cadastro de usuários. Deve haver, no mínimo, 3 tipos de usuários:

# Administrador
# Vendedor
# Cliente
# Deve ser possível também usuários não autenticados acessarem a plataforma para visualizar informações sobre os produtos.

# Funcionalidades permitidas para os clientes:
# Pode atualizar o perfil para se tornar vendedor.
# Adicionar produtos ao carrinho.
# Finalizar a compra dos produtos.
# Deve ter uma rota para visualizar todos os pedidos comprados.
