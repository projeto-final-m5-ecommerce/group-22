from rest_framework import generics, status
from rest_framework.response import Response
from .models import Cart
from .serializers import CartSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from users.models import User


class CartListView(generics.ListAPIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    serializer_class = CartSerializer
    queryset = Cart.objects.all()
    # request.user.Cart.Products

    # def get_queryset(self, *args, **kwargs):
    #     user = super().get_queryset(*args, **kwargs)
    #     user.filter(user=self.request.user)

    #     return user

    def perform_create(self, serializer):
        get_user = get_object_or_404(User, id=self.request.user.id)
        # serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)

        # cart_products = serializer.validated_data["cart_products"]
        # for item in cart_products:
        #     if item.product.stock < item.quantity:
        #         return Response(
        #             {"error": f"Produto {item.product.name} sem estoque suficiente"},
        #             status=status.HTTP_400_BAD_REQUEST,
        #         )
        serializer.save(user=get_user)
        # self.perform_create(serializer)
        # headers = self.get_success_headers(serializer.data)
        # return Response(
        #     serializer.data, status=status.HTTP_201_CREATED, headers=headers
        # )

    # def perform_create(self, serializer):
    #     cart_products = serializer.validated_data["cart_products"]
    #     total = sum(item.product.price * item.quantity for item in cart_products)
    #     serializer.save(total=total)


class CartRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    serializer_class = CartSerializer
    queryset = Cart.objects.all()

    def perform_update(self, serializer):
        cart = serializer.save()
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
            else:
                product.stock -= quantity
                product.save()

    def perform_destroy(self, instance):
        for cart_product in instance.cart_products.all():
            product = cart_product.product
            quantity = cart_product.quantity
            product.stock += quantity
            product.save()
        instance.delete()
