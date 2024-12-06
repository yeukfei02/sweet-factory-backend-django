from django.db import models
from users.models import User
from cities.models import City


class Machine(models.Model):
    machine_name = models.TextField()
    serial_number = models.IntegerField()
    created_at = models.DateTimeField("created_at", auto_now_add=True)
    updated_at = models.DateTimeField("updated_at", auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    class Meta:
        db_table = 'machines'
        indexes = [
            models.Index(fields=['machine_name']),
            models.Index(fields=['serial_number']),
            models.Index(fields=['created_at']),
            models.Index(fields=['updated_at']),
            models.Index(fields=['user_id']),
            models.Index(fields=['city_id']),
        ]
