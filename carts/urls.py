from django.urls import path

from . import views

urlpatterns = [
    path("cart/", views.CartListCreateView.as_view()),
    # path("carts/<int:pk>/update", views.CartRetrieveUpdateDestroyView.as_view()),
]
