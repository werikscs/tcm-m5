from django.urls import path
from . import views

urlpatterns = [
     path("users/<int:user_id>/wishlist/", views.UserWishlistView.as_view()),
     path("users/<int:user_id>/wishlist/<int:wishlist_id>/", views.UserWishlistDetailView.as_view()),
     
]