from django.urls import path
from . import views

urlpatterns = [
     path("cart/<int:cart_id>/", views.CartView.as_view()),
]
     