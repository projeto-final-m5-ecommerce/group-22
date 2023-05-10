from rest_framework import serializers
from .models import Order
from carts.models import Cart
from django.core.mail import send_mail
from django.conf import settings
from carts.serializers import ProductsCartSerializer


class CartOrderSerializer(serializers.ModelSerializer):
    cart_products = ProductsCartSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ["cart_products"]


class OrderSerializer(serializers.ModelSerializer):
    cart = CartOrderSerializer(read_only=True)
    total = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ["id", "ordered_time", "status", "user", "cart", "total"]
        read_only_fields = ["id", "user", "ordered_time", "cart", "total"]

    def get_total(self, obj):
        id_user = obj.user.id
        filtered_cart = Cart.objects.filter(user=id_user)
        user_cart = filtered_cart[0].cart_products.all()
        all_values = [product.price for product in user_cart]
        return sum(all_values)

    def create(self, validated_data):
        return Order.objects.create(**validated_data)

    def update(self, instance, validated_data):
        order_user_email = instance.user.email

        for key, value in validated_data.items():
            if key == "status" and value != "Order placed":
                send_mail(
                    subject="Order Status",
                    message=f"Your order status has been updated to {value}.",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[order_user_email],
                    fail_silently=False,
                )
                setattr(instance, key, value)

        instance.save()

        return instance
