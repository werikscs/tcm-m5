from django.urls import path

from .views import DiscountView, DiscountDetailView

urlpatterns = [
    path("discount/", DiscountView.as_view()),
    path("discount/<pk>/", DiscountDetailView.as_view())
]
