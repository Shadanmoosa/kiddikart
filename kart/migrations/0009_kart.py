# Generated by Django 5.0.3 on 2024-04-27 14:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kart', '0008_delete_kart'),
    ]

    operations = [
        migrations.CreateModel(
            name='kart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('size', models.CharField(max_length=10)),
                ('productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kart.products')),
                ('profileid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kart.userprofile')),
            ],
        ),
    ]
