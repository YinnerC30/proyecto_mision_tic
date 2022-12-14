# Generated by Django 4.1.1 on 2022-09-30 07:38

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Categorias",
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
                ("categoria", models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name="Books",
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
                ("titulo", models.CharField(max_length=200)),
                ("categoria", models.CharField(max_length=200)),
                ("estado", models.CharField(max_length=15)),
                ("autor", models.CharField(max_length=200)),
                ("reseña", ckeditor.fields.RichTextField(blank=True, null=True)),
                (
                    "libro_img",
                    models.ImageField(blank=True, null=True, upload_to="images/"),
                ),
                ("fecha", models.DateTimeField(auto_now_add=True)),
                (
                    "likes",
                    models.ManyToManyField(
                        related_name="book_post", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
