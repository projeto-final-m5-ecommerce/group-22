from rest_framework import serializers
from .models import Order
from carts.models import Cart
from django.core.mail import send_mail
from django.conf import settings
from products.serializers import ProductSerializer

import ipdb


class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
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
        user_email = self.user.email

        for key, value in validated_data.items():
            # so vendedor pode alterar status
            if key == "status" and value != "Order placed":
                send_mail(
                    subject="Order Status",
                    message="Your order status has been updated.",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[user_email],
                    fail_silently=False,
                )
                setattr(instance, key, value)

        instance.save()

        return instance
