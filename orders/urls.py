from django.urls import path

from .views import OrderView

urlpatterns = [
    # criar ordem de user ou pegar todas as ordens do user
    path("order/<int:user_id>/", OrderView.as_view()),
    # pegar ordem específica de user
    # path("order/<int:user_id>/<int:order_id>/", ),
]
