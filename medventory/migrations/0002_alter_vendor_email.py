# Generated by Django 4.2.11 on 2024-04-23 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='email',
            field=models.EmailField(max_length=64),
        ),
    ]