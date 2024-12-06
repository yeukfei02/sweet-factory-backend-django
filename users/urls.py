from django.urls import path

from . import views

urlpatterns = [
    path("signup", views.signup, name="signup"),
    path("login", views.login, name="login"),
    path("", views.get_users, name="get_users"),
    path("user/<int:id>", views.get_user, name="get_user"),
]
