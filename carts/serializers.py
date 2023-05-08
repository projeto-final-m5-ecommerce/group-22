from rest_framework import serializers
from .models import Cart, ProductsCart
from products.models import Product


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "category", "price"]


class CartUpdateSerializer(serializers.ModelSerializer):
    product = ProductsSerializer()

    class Meta:
        model = ProductsCart
        fields = ["product", "quantity"]

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class CartSerializer(serializers.ModelSerializer):
    # product = ProductsSerializer()

    class Meta:
        model = Cart
        fields = ["product", "quantity"]
        # read_only_fields = ["id", ]

    def create(self, validated_data):
        return Cart.objects.create(**validated_data)


class CartDetailSerializer(serializers.ModelSerializer):
    # total = serializers.SerializerMethodField()
    # cart = CartSerializer()

    class Meta:
        model = ProductsCart
        fields = "__all__"
        # exclude = ["available", "stock"]
        depth = 1


"""     def get_total(self, obj):
        all_products = obj.cart_products.all()
        all_values = [product.price for product in all_products]
        return sum(all_values)
 """
