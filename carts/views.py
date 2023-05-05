from rest_framework import generics
from .models import Cart
from .serializers import CartSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from products.models import Product


class CartListView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = CartSerializer
    queryset = Cart.objects.all()


class CartUpdateView(generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = CartSerializer
    queryset = Product.objects.all()

    def get_object(self):
        user_cart = get_object_or_404(Cart, user=self.request.user)
        return user_cart

    def perform_update(self, serializer):
        user_cart = self.request.user.cart.cart_products
        product = Product.objects.get(id=self.kwargs.get("pk"))
        user_cart.add(product)
        serializer.save()

    # def get_queryset(self):
    #     pk = self.kwargs.get("pk")
    #     ipdb.set_trace()

    #    return querysetr

    # for cart_product in cart.cart_products.all():
    #     product = cart_product.product
    #     quantity = cart_product.quantity
    #     if product.stock < quantity:
    #         cart_product.available = False
    #         cart_product.save()
    #         return Response(
    #             {
    #                 "message": f"Product '{product.name}' is not available in the requested quantity."
    #             },
    #             status=status.HTTP_400_BAD_REQUEST,
    #         )
    #     else:
    #         product.stock -= quantity
    #         product.save()
