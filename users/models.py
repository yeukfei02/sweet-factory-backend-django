from django.db import models


class User(models.Model):
    email = models.TextField(unique=True)
    password = models.TextField()
    created_at = models.DateTimeField("created_at", auto_now_add=True)
    updated_at = models.DateTimeField("updated_at", auto_now=True)

    class Meta:
        db_table = 'users'
        indexes = [
            models.Index(fields=['email']),
            models.Index(fields=['password']),
            models.Index(fields=['created_at']),
            models.Index(fields=['updated_at']),
        ]
