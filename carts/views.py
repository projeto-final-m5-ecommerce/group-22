from rest_framework import generics
from .models import Cart
from .serializers import CartSerializer, CartListSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from products.models import Product


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
        user_cart = self.get_object()
        product = Product.objects.get(id=self.kwargs.get("pk"))
        user_cart.cart_products.add(product)
        serializer.save()
