# Generated by Django 4.1.1 on 2022-09-26 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0013_categorias"),
    ]

    operations = [
        migrations.AlterField(
            model_name="books",
            name="categoria",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="books", name="estado", field=models.CharField(max_length=15),
        ),
    ]