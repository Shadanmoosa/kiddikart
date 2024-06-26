# Generated by Django 5.0.3 on 2024-04-29 15:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kart', '0016_kart'),
    ]

    operations = [
        migrations.CreateModel(
            name='wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kart.products')),
                ('profileid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kart.userprofile')),
            ],
        ),
    ]
