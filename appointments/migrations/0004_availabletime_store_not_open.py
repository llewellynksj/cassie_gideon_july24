# Generated by Django 3.2.20 on 2023-08-19 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0003_auto_20230819_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='availabletime',
            name='store_not_open',
            field=models.BooleanField(default=False),
        ),
    ]