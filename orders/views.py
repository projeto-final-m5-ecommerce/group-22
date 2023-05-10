from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from carts.models import Cart
from products.permissions import IsAdminOrSeller


class OrderView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        user_cart = get_object_or_404(Cart, user=self.request.user)

        return serializer.save(user=self.request.user, cart=user_cart)


class OrderUpdateView(generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrSeller]

    serializer_class = OrderSerializer
    queryset = Order.objects.all()
