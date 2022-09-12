from django.urls import path

from .views import DiscountView, DiscountDetailView

urlpatterns = [
    path("discount/", DiscountView.as_view()),
    path("discount/<int:discount_id>/", DiscountDetailView.as_view())
]
