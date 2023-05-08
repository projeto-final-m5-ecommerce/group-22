from rest_framework import serializers
from .models import Order
from carts.models import Cart

# import ipdb


class OrderSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()
    total = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ["id", "ordered_time", "status", "user", "products", "total"]
        read_only_fields = ["id", "user", "ordered_time", "products", "total"]

    def get_products(self, obj):
        id_user = obj.user.id
        filtered_cart = Cart.objects.filter(user=id_user)
        user_cart = filtered_cart[0].cart_products.all()

        list_products = []

        for product in user_cart:
            product_details = {
                "name": product.name,
                "category": product.category,
                "price": product.price,
            }
            list_products.append(product_details)

        return list_products

    def get_total(self, obj):
        id_user = obj.user.id
        filtered_cart = Cart.objects.filter(user=id_user)
        user_cart = filtered_cart[0].cart_products.all()
        all_values = [product.price for product in user_cart]
        return sum(all_values)

    def create(self, validated_data):
        return Order.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            # so vendedor pode alterar status
            setattr(instance, key, value)

        instance.save()

        return instance
