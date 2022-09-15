from django.urls import path

from .views import CategoryDetailView, CategoryView

urlpatterns = [
    path("category/", CategoryView.as_view()),
    path("category/<pk>/", CategoryDetailView.as_view()),
]
