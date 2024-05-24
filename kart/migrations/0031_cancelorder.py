# Generated by Django 5.0.3 on 2024-05-23 23:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kart', '0030_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='cancelorder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='order')),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('size', models.CharField(max_length=10)),
                ('total', models.DecimalField(decimal_places=2, max_digits=9)),
                ('orderdate', models.CharField(max_length=100)),
                ('packed', models.IntegerField(default=0)),
                ('packeddate', models.CharField(max_length=100)),
                ('delivered', models.IntegerField(default=0)),
                ('delivereddate', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kart.addressmodel')),
                ('productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kart.products')),
                ('profileid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kart.userprofile')),
                ('sellerid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kart.userdatabase')),
            ],
        ),
    ]
