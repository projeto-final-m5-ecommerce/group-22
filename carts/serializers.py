from rest_framework import serializers
from .models import Cart

# from products.serializers import ProductSerializer
from products.models import Product
import ipdb


class ProductsCartSerializer(serializers.ModelSerializer):
    # quantity = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ["id", "name", "category", "user", "price", "quantity"]

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)

    #     if representation["quantity"] >= 0:
    #         sum([representation["quantity"], 1])

    #     return representation

    # def get_quantity(self, obj):
    #     sum_count = 0
    #     # ipdb.set_trace()

    #     acc= sum_count += 1
    #     return acc


class CartListSerializer(serializers.ModelSerializer):
    cart_products = ProductsCartSerializer(many=True, read_only=True)
    total = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ["cart_products", "id", "user", "total"]

        read_only_fields = ["id", "user", "total"]

    def get_total(self, obj):
        # ipdb.set_trace()
        all_products = obj.cart_products.all()
        all_values = [product.price for product in all_products]
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
        all_values = [product.price for product in all_products]
        return sum(all_values)

    # def get_cart_products(self, obj):
    #     cart_products = obj.cart_products.all()
    #     ipdb.set_trace()
    #     serialized_cart_products = []
    #     for cart_product in cart_products:
    #         serialized_cart_product = {
    #             "id": cart_product.id,
    #             "name": cart_product.name,
    #             "category": cart_product.category,
    #             "price": cart_product.price,
    #             "quantity": cart_product.quantity,
    #         }
    #         serialized_cart_products.append(serialized_cart_product)
    #     return serialized_cart_products
