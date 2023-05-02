from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Product


class UserSerializer(serializers.ModelSerializer):
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
            "price ",
            "stock",
            "available",
            "user_id ",
        ]
        read_only_fields = [
            "id",
            "user_id ",
        ]

    def create(self, validated_data):
        return Product.objects.create_superuser(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
