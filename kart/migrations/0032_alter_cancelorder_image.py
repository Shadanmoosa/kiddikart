# Generated by Django 5.0.3 on 2024-05-23 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kart', '0031_cancelorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancelorder',
            name='image',
            field=models.ImageField(upload_to='cancel'),
        ),
    ]
