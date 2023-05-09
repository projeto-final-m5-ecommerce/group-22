from rest_framework import generics
from .models import Cart
from .serializers import CartSerializer, CartListSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from products.models import Product

from rest_framework import serializers


class CartListView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CartListSerializer

    def get_queryset(self):
        user = self.request.user
        return Cart.objects.filter(user=user)


class CartUpdateView(generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CartSerializer
    queryset = Cart.objects.all()

    def get_object(self):
        user_cart = get_object_or_404(Cart, user=self.request.user)
        return user_cart

    def perform_update(self, serializer):
        cart = self.get_object()

        cart_product = cart.cart_products.all()

        if cart_product:
            for product in cart_product:
                if product.id == self.kwargs.get("pk"):
                    product.quantity += 1
                    if product.quantity > product.stock:
                        message = (
                            f"Insufficient amount of {product.name} product available."
                        )
                        raise serializers.ValidationError(
                            message,
                            code="invalid",
                        )
                    product.save()
                else:
                    current_product = Product.objects.get(id=self.kwargs.get("pk"))
                    cart.cart_products.add(current_product)

        serializer.save()
