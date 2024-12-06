# Generated by Django 5.1.4 on 2024-12-05 13:37

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.CharField()),
                ("password", models.CharField()),
                ("created_at", models.DateTimeField(verbose_name="created_at")),
                ("updated_at", models.DateTimeField(verbose_name="updated_at")),
            ],
        ),
    ]
