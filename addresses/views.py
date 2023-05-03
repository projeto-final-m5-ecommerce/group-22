from django.shortcuts import render
from rest_framework import generics

from addresses.serializers import AddressSerializer


class AddressView(generics.CreateAPIView):
    serializer_class = AddressSerializer
