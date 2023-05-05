from rest_framework import serializers
from .models import Cart

# from ..products.models import Product
import ipdb


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"


# def update(self, instance, validated_data):
# acessar o usuario para fazer o update no carrinho do usuario, preciso do pk da url
# ipdb.set_trace()


# read_only_fields = ["id", "user_id", "total"]
