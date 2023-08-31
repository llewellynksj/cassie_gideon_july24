# Generated by Django 3.2.20 on 2023-08-20 13:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appointments', '0006_auto_20230819_1240'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_guests', models.PositiveIntegerField(help_text='Note you may bring up to 5 guests in addition to yourself')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_email', to=settings.AUTH_USER_MODEL)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_name', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AvailableDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('available', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='AvailableTimeSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Morning Appointment', 'Morning Appointment'), ('Lunchtime Appointment', 'Lunchtime Appointment'), ('Afternoon Appointment', 'Afternoon Appointment')], max_length=50)),
                ('time', models.TimeField()),
                ('available', models.BooleanField(default=False)),
                ('duration_in_minutes', models.PositiveIntegerField(default=120)),
            ],
        ),
        migrations.DeleteModel(
            name='AppointmentType',
        ),
        migrations.DeleteModel(
            name='AvailableDay',
        ),
        migrations.DeleteModel(
            name='AvailableTime',
        ),
    ]