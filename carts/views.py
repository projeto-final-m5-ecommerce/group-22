from rest_framework import generics, status
from rest_framework.response import Response
from .models import Cart
from .serializers import CartSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class CartView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = CartSerializer

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def get_serializer(self, *args, **kwargs):
        kwargs["many"] = True
        return super().get_serializer(*args, **kwargs)

    def perform_create(self, serializer):
        cart = serializer.save(user=self.request.user)
        for cart_product in cart.cart_products.all():
            product = cart_product.product
            quantity = cart_product.quantity
            if product.stock < quantity:
                cart_product.available = False
                cart_product.save()
                return Response(
                    {
                        "message": f"Product '{product.name}' is not available in the requested quantity."
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
