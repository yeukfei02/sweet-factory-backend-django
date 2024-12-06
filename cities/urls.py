from django.urls import path

from . import views

urlpatterns = [
    path("create-city", views.create_city, name="create_city"),
    path("get-cities", views.get_cities, name="get_cities"),
    path("<int:id>", views.get_city, name="get_city"),
]
