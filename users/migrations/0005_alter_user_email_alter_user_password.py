# Generated by Django 5.1.4 on 2024-12-05 15:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_alter_user_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.TextField(),
        ),
    ]
