from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=128)
    number = models.IntegerField()
    city = models.CharField(max_length=128)
    state = models.CharField(max_length=128)

    user = models.OneToOneField(
        "users.User", on_delete=models.CASCADE, related_name="address"
    )


# Usuário deve ter uma relacionamento com um campo de endereço.
