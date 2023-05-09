from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404

from .serializers import ProductSerializer
from .models import Product
from users.models import User
from .permissions import IsAdminOrSeller


class ProductView(ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    pagination_class = PageNumberPagination
    permission_classes = [IsAdminOrSeller]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "name",
        "category",
        "id",
    ]

    def perform_create(self, serializer):
        get_user = get_object_or_404(User, id=self.request.user.id)

        serializer.save(user=get_user)


class ProductDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_update(self, serializer):
        serializer.partial = True
        serializer.save()
