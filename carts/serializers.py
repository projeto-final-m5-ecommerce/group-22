from rest_framework import serializers
from .models import Cart, CartProduct


class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProduct
        fields = ["product", "quantity", "seller"]


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
            CartProduct.objects.create(cart=cart, **product_data)
        return cart

    def update(self, instance, validated_data):
        cart_products_data = validated_data.pop("cart_products", [])
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()

        # Delete
        cart_products_ids = [item["id"] for item in cart_products_data if "id" in item]
        instance.cart_products.exclude(id__in=cart_products_ids).delete()

        # Update
        for product_data in cart_products_data:
            if "id" in product_data:
                cart_product = CartProduct.objects.get(
                    id=product_data["id"], cart=instance
                )
                for key, value in product_data.items():
                    setattr(cart_product, key, value)
                cart_product.save()
            else:
                CartProduct.objects.create(cart=instance, **product_data)

        return instance
