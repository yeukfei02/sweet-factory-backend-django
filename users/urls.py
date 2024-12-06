from django.urls import path

from . import views

urlpatterns = [
    path("create-user", views.create_user, name="create_user"),
    path("", views.get_users, name="get_users"),
    path("user/<int:id>", views.get_user, name="get_user"),
]
