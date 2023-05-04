from rest_framework import generics, status
from rest_framework.response import Response
from .models import Cart
from .serializers import CartSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class CartView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = CartSerializer

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.first()
        if not obj:
            obj = Cart.objects.create(user=self.request.user)
        return obj

    def put(self, request, *args, **kwargs):
        cart = self.get_object()
        serializer = self.get_serializer(cart, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        for cart_product in serializer.validated_data["cart_products"]:
            product = cart_product["product"]
            seller = cart_product["seller"]
            quantity = cart_product["quantity"]
            if product.stock < quantity or product.seller != seller:
                return Response(
                    {
                        "message": f"Product '{product.name}' is not available in the requested quantity or from the selected seller."
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
