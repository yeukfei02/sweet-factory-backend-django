from django.urls import path

from . import views

urlpatterns = [
    path("create-machine", views.create_machine, name="create_machine"),
    path("get-machines", views.get_machines, name="get_machines"),
    path("<int:id>", views.get_machine, name="get_machine"),
]
