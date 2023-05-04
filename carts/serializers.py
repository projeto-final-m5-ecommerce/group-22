from rest_framework import serializers
from .models import Cart


class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart.cart_products
        fields = ["product", "quantity"]


class CartSerializer(serializers.ModelSerializer):
    cart_products = CartProductSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = [
            "id",
            "total",
            "user",
            "cart_products",
        ]

    def create(self, validated_data):
        cart_products_data = validated_data.pop("cart_products")
        cart = Cart.objects.create(**validated_data)
        for product_data in cart_products_data:
            Cart.cart_products.objects.create(cart=cart, **product_data)
        return cart
