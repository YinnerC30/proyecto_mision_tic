# Generated by Django 4.1.1 on 2022-10-04 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_books_intencion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='intencion',
            field=models.CharField(max_length=200),
        ),
    ]
