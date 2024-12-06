# Generated by Django 5.1.4 on 2024-12-06 14:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cities", "0002_city_cities_city_na_2ea01e_idx_and_more"),
        ("machines", "0001_initial"),
        ("users", "0006_user_users_email_4b85f2_idx_and_more"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="machine",
            index=models.Index(
                fields=["machine_name"], name="machines_machine_eb565c_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="machine",
            index=models.Index(
                fields=["serial_number"], name="machines_serial__83a8bb_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="machine",
            index=models.Index(
                fields=["created_at"], name="machines_created_07be7e_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="machine",
            index=models.Index(
                fields=["updated_at"], name="machines_updated_ed3f0b_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="machine",
            index=models.Index(fields=["user_id"], name="machines_user_id_e76dca_idx"),
        ),
        migrations.AddIndex(
            model_name="machine",
            index=models.Index(fields=["city_id"], name="machines_city_id_ea3a33_idx"),
        ),
    ]
