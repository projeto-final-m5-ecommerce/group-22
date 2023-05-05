from django.urls import path
from . import views

urlpatterns = [
    path("product/", views.ProductView.as_view()),
    path("product/<int:pk>/", views.ProductDetailView.as_view()),
<<<<<<< HEAD
    # path("products/<int:pk>/update", views.UserUpdateTypeView.as_view()),
=======
>>>>>>> 21f38fa247731a8bbe45c5295beb9dd5f8625af6
]
