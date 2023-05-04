from django.shortcuts import render
from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer
from ..carts.models import Cart
from ..users.models import User


class OrderView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        # cart_id = self.kwargs.get("pk")
        # cart = Cart.objects.filter(id=cart_id).values()
        # list_products = cart.

        # user = self.request.user.
        # list_products = user.

        # serializer.save()
        return serializer.save(user_id=self.kwargs.get("pk"))
