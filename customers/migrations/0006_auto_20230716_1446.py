# Generated by Django 3.2.20 on 2023-07-16 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_alter_customer_wedding_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='wedding_date',
        ),
        migrations.AddField(
            model_name='customer',
            name='bio',
            field=models.TextField(default='none'),
            preserve_default=False,
        ),
    ]
