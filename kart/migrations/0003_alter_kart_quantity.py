# Generated by Django 5.0.3 on 2024-04-17 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kart', '0002_kart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kart',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
