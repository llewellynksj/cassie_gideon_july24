# Generated by Django 3.2.20 on 2023-07-29 13:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0003_auto_20230729_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='favourites',
            field=models.ManyToManyField(blank=True, related_name='product_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]