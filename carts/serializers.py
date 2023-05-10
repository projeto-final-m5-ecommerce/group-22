from rest_framework import serializers
from .models import Cart


from products.models import Product


class ProductsCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "category", "user", "price", "quantity"]


class CartListSerializer(serializers.ModelSerializer):
    cart_products = ProductsCartSerializer(many=True, read_only=True)
    total = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ["cart_products", "id", "user", "total"]

        read_only_fields = ["id", "user", "total"]

    def get_total(self, obj):
        all_products = obj.cart_products.all()

        all_values = [product.price * product.quantity for product in all_products]
        return sum(all_values)


class CartSerializer(serializers.ModelSerializer):
    cart_products = ProductsCartSerializer(many=True, read_only=True)
    total = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ["cart_products", "total"]
        read_only_fields = ["id", "user", "total"]

        depth = 1

    def get_total(self, obj):
        all_products = obj.cart_products.all()
        all_values = [product.price * product.quantity for product in all_products]
        return sum(all_values)
