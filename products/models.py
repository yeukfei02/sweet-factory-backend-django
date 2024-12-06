from django.db import models
from users.models import User
from cities.models import City
from machines.models import Machine


class Product(models.Model):
    product_name = models.TextField()
    product_description = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField()
    created_at = models.DateTimeField("created_at", auto_now_add=True)
    updated_at = models.DateTimeField("updated_at", auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)

    class Meta:
        db_table = 'products'
