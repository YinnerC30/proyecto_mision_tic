# Generated by Django 4.1.1 on 2022-10-04 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_delete_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='editorial',
            field=models.CharField(max_length=50, null=True),
        ),
    ]