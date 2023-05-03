from django.shortcuts import render
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.models import User
from users.permissions import IsAdmin
from users.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


class UserView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        serializer.partial = True
        serializer.save()

class UserUpdateTypeView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdmin]
