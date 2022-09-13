from django.urls import path
from . import views

urlpatterns = [
     path("cart/add/", views.CartProductsView.as_view()),
]