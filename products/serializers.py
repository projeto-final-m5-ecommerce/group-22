from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=Product.objects.all(),
                message="A product with that name already exists.",
            )
        ],
    )

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "category",
            "price",
            "stock",
            "available",
            "user_id",
        ]
        read_only_fields = [
            "id",
            "user_id",
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if representation["stock"] is 0:
            representation["available"] = representation["available"] == False

        return representation

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        if self.stock > 0:
            self.available = True
        else:
            self.available = False

        instance.save()
        return instance
