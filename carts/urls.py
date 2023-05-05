from django.urls import path

from . import views

urlpatterns = [
    path("cart/", views.CartListView.as_view()),
    path("cart/product/<int:pk>/", views.CartUpdateView.as_view()),
]
