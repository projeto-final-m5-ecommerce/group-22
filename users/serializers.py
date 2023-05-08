from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from addresses.models import Address
from carts.models import Cart
from addresses.serializers import AddressSerializer
from .models import User


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="A user with that username already exists.",
            )
        ],
    )
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())],
    )

    address = AddressSerializer()

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "is_seller",
            "address",
        ]
        read_only_fields = [
            "id",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data: dict) -> User:
        address_data = validated_data.pop("address")

        user = User.objects.create_user(**validated_data)

        cart = Cart.objects.create(user=user)

        address = Address.objects.create(user=user, **address_data)

        return user

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        new_password = validated_data.pop("password", "")

        if new_password:
            instance.set_password(new_password)

        instance.save()

        return instance
