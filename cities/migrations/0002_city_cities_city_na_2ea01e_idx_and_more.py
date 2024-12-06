# Generated by Django 5.1.4 on 2024-12-06 14:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cities", "0001_initial"),
        ("users", "0006_user_users_email_4b85f2_idx_and_more"),
        ("zones", "0002_zone_zones_zone_na_c5113f_idx_and_more"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="city",
            index=models.Index(fields=["city_name"], name="cities_city_na_2ea01e_idx"),
        ),
        migrations.AddIndex(
            model_name="city",
            index=models.Index(fields=["area"], name="cities_area_98b45f_idx"),
        ),
        migrations.AddIndex(
            model_name="city",
            index=models.Index(fields=["created_at"], name="cities_created_319911_idx"),
        ),
        migrations.AddIndex(
            model_name="city",
            index=models.Index(fields=["updated_at"], name="cities_updated_05b33e_idx"),
        ),
        migrations.AddIndex(
            model_name="city",
            index=models.Index(fields=["user_id"], name="cities_user_id_1602ab_idx"),
        ),
        migrations.AddIndex(
            model_name="city",
            index=models.Index(fields=["zone_id"], name="cities_zone_id_4f54f6_idx"),
        ),
    ]
