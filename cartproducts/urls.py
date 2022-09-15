from django.urls import path
from . import views

urlpatterns = [
     path("cart/add/", views.CartProductsView.as_view()),
     path("cart/remove/<int:cartproduct_id>/", views.CartProductsDetailView.as_view()),
]