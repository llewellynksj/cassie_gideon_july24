from django.db import models
from datetime import datetime
from customers.models import Customer
from django.contrib.auth.models import User


class Appointment(models.Model):
    name = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user_name')
    email = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user_email')
    no_of_guests = models.PositiveIntegerField(help_text='Note you may bring up to 5 guests in addition to yourself') 
    date = models.DateField(auto_now=False)
    time = models.TimeField(auto_now=False)

    def __str__(self):
        return str(self.name) + (self.date)


class AvailableDate(models.Model):
    date = models.DateField(auto_now=False)
    available = models.BooleanField(default=False)
    test_text = models.CharField(default='This is from the model', max_length=100)

    def __str__(self):
        return str(self.date)
    
    @property
    def get_available_dates(self):
        if self.available == True:
            return str(self.date)


class AvailableTimeSlot(models.Model):
    SLOT_TYPE = [
        ('Morning Appointment', 'Morning Appointment'),
        ('Lunchtime Appointment', 'Lunchtime Appointment'),
        ('Afternoon Appointment', 'Afternoon Appointment'),
    ]

    type = models.CharField(max_length=50, choices=SLOT_TYPE)
    time = models.TimeField(auto_now=False)
    available = models.BooleanField(default=False)
    duration_in_minutes = models.PositiveIntegerField(default=120)

    def __str__(self):
        return self.type


# class AvailableTime(models.Model):
#     DAYS = [
#         ('Monday', 'Monday'),
#         ('Tuesday', 'Tuesday'),
#         ('Wednesday', 'Wednesday'),
#         ('Thursday', 'Thursday'),
#         ('Friday', 'Friday'),
#         ('Saturday', 'Saturday'),
#         ('Sunday', 'Sunday'),
#     ]
#     day = models.CharField(max_length=30, choices=DAYS, default='Monday')
#     start_time = models.TimeField(auto_now=False, help_text='Enter the time you wish your calendar to open for bookings', blank=True, null=True)
#     end_time = models.TimeField(auto_now=False, help_text='Enter the time you wish your calendar to close for bookings', blank=True, null=True)
#     store_not_open = models.BooleanField(default=False)

#     def __str__(self):
#         return self.day
