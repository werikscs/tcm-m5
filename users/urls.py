from django.urls import path
from . import views

urlpatterns = [
     path("users/", views.UserRegisterView.as_view()),
     path("users/registerstaff/", views.UserRegisterStaff.as_view()),
     path("users/login/", views.LoginView.as_view()),
     path("users/<int:user_id>/", views.UserDetailView.as_view()),
     path("users/<int:user_id>/deleteorchange/", views.UserDeleteOrChangeView.as_view()),
]