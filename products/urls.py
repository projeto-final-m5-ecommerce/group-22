from django.urls import path
from . import views

urlpatterns = [
    path("product/", views.ProductView.as_view()),
    path("product/<int:pk>/", views.ProductDetailView.as_view()),
]
