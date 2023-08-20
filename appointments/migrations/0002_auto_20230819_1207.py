# Generated by Django 3.2.20 on 2023-08-19 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvailableDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_commencing', models.DateField()),
                ('monday', models.BooleanField()),
                ('tuesday', models.BooleanField()),
                ('wednesday', models.BooleanField()),
                ('thursday', models.BooleanField()),
                ('friday', models.BooleanField()),
                ('saturday', models.BooleanField()),
                ('sunday', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='AvailableTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField(help_text='Enter the time you wish your calendar to open for bookings')),
                ('end_time', models.TimeField(help_text='Enter the time you wish your calendar to close for bookings')),
            ],
        ),
        migrations.DeleteModel(
            name='AvailableDays',
        ),
        migrations.AlterField(
            model_name='appointmenttype',
            name='appointment_name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
