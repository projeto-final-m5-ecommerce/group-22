from django.shortcuts import render
from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer
import ipdb
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class OrderView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        # users = User.objects.all()[0]
        user = self.request.user.cart
        ipdb.set_trace()
        # list_products = user.

        # serializer.save()
        return serializer.save(user_id=self.request.user.id)
