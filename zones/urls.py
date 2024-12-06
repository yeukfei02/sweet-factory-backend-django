from django.urls import path

from . import views

urlpatterns = [
    path("create-zone", views.create_zone, name="create_zone"),
    path("get-zones", views.get_zones, name="get_zones"),
    path("<int:id>", views.get_zone, name="get_zone"),
]
