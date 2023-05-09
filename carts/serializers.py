from rest_framework import serializers
from .models import Cart
from products.serializers import ProductSerializer


class CartListSerializer(serializers.ModelSerializer):
    cart_products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ["cart_products", "id", "user", "total"]

        read_only_fields = ["id", "user", "total"]


class CartSerializer(serializers.ModelSerializer):
    cart_products = serializers.SerializerMethodField()
    total = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ["cart_products", "total"]
        read_only_fields = ["id", "user", "total"]

    def get_total(self, obj):
        all_products = obj.cart_products.all()
        all_values = [product.price for product in all_products]
        return sum(all_values)

    def get_cart_products(self, obj):
        all_products = obj.cart_products.all()
        result = []
        for product in all_products:
            product_serialized = {
                "name": product.name,
                "category": product.category,
                "price": product.price,
                "quantity": 1,
            }
            result.append(product_serialized)
        return result
