from django.urls import path

from . import views

urlpatterns = [
    path("create-product", views.create_product, name="create_product"),
    path("get-products", views.get_products, name="get_products"),
    path("<int:id>", views.get_product, name="get_product"),
]
