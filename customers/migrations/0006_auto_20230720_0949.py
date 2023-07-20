# Generated by Django 3.2.20 on 2023-07-20 09:49

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_auto_20230720_0827'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='profile_pic',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='customer',
            name='website_url',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
