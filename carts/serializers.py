from rest_framework import serializers
from .models import Cart

# from ..products.models import Product
import ipdb


class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model: Cart.cart_products
        fields = "__all__"

    def create(self, validated_data) -> Cart:
        return Cart.create(**validated_data)


class CartSerializer(serializers.ModelSerializer):
    cart_products = CartProductSerializer(many=True)

    class Meta:
        model = Cart
        fields = ["id", "user_id", "total"]
        read_only_fields = ["id", "user_id", "total"]

    def create(self, validated_data):
        # cart_products_data = validated_data.pop("cart_products")
        # print(50 * "-")
        # print(cart_products_data)
        # print(50 * "-")
        # ipdb.set_trace()
        # for item_data in cart_products_data:
        #     product_id = item_data.pop("product")
        #     product = "products.Product".objects.get(id=product_id)
        #     if product.stock < item_data["quantity"]:
        #         raise serializers.ValidationError(
        #             f"Produto {product.name} sem estoque suficiente"
        #         )
        #     Cart.cart_products.object.create(product=product, **item_data)
        # cart = Cart.objects.create(**validated_data)
        return Cart.objects.create(**validated_data)

    # def to_representation(self, instance):
    #     ret = super().to_representation(instance)
    #     ret["cart_products"] = [item["product"] for item in ret["cart_products"]]
    #     return ret
