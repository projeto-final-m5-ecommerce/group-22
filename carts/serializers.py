from rest_framework import serializers
from .models import Cart


class CartSerializer(serializers.ModelSerializer):
    cart_products = serializers.SerializerMethodField()
    total = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ["cart_products", "total"]
        read_only_fields = ["id", "user_id", "total"]

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
