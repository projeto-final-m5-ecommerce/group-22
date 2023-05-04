from django.urls import path
from . import views
from products import views as product_views


from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("users/", views.UserView.as_view()),
    path("users/<int:pk>/", views.UserDetailView.as_view()),
    path("users/<int:pk>/update", views.UserUpdateTypeView.as_view()),
    path("users/login/", jwt_views.TokenObtainPairView.as_view()),
    path("users/<int:pk>/product/", product_views.ProductView.as_view()),
]
