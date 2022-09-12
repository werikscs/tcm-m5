from django.urls import path

from .views import CategoryView, CategoryDetailView

urlpatterns = [
    path("category/", CategoryView.as_view()),
    path("category/<int:category_id>/", CategoryDetailView.as_view())
]
