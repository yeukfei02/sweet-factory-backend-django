from django.db import models
from users.models import User
from zones.models import Zone


class City(models.Model):
    city_name = models.TextField()
    area = models.TextField()
    created_at = models.DateTimeField("created_at", auto_now_add=True)
    updated_at = models.DateTimeField("updated_at", auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)

    class Meta:
        db_table = 'cities'
