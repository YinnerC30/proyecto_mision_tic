# Generated by Django 4.1.1 on 2022-09-15 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("login", "0002_delete_user"),
    ]

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
                ("nombre", models.CharField(max_length=30)),
                ("apellidos", models.CharField(max_length=30)),
                ("contraseña", models.TextField(max_length=30)),
            ],
        ),
    ]