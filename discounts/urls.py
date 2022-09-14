from django.urls import path

from .views import DiscountDetailView, DiscountView

urlpatterns = [
    path("discount/", DiscountView.as_view()),
    path("discount/<pk>/", DiscountDetailView.as_view()),
]
