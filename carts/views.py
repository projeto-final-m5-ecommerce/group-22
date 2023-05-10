from rest_framework import generics, status
from .models import Cart
from .serializers import CartSerializer, CartListSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from products.models import Product
from rest_framework.exceptions import ValidationError, APIException


class CustomValidationError(APIException):
    status_code = status.HTTP_403_FORBIDDEN


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

        current_product = Product.objects.get(id=self.kwargs.get("pk"))
        if cart.user_id == current_product.user_id:
            message = f"It is not possible to add your own product to the cart."
            raise CustomValidationError(detail=message)

        if cart_product:
            for product in cart_product:
                if product.id == self.kwargs.get("pk"):
                    product.quantity += 1
                    if product.quantity > product.stock:
                        message = (
                            f"Insufficient amount of {product.name} product available."
                        )
                        raise ValidationError(
                            message,
                            code=status.HTTP_400_BAD_REQUEST,
                        )
                    product.save()

        current_product = Product.objects.get(id=self.kwargs.get("pk"))
        cart.cart_products.add(current_product)
        serializer.save()
