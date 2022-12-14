from django.urls import path

from .views import ProductCategoryView, ProductDetailView, ProductView

urlpatterns = [
    path("products/", ProductView.as_view()),
    path("products/<pk>/", ProductDetailView.as_view()),
    path("products/category/<int:category_id>/", ProductCategoryView.as_view()),
]
