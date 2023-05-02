from rest_framework import serializers
from .models import Cart


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = [
            "id",
            "name",
            "price",
            "category",
            "ordered_time",
            "status",
            "user_id",
        ]
        read_only_fields = ["id", "user_id", "ordered_time"]

    def create(self, validated_data):
        return Cart.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            # so vendedor pode alterar status
            setattr(instance, key, value)

        instance.save()

        return instance
