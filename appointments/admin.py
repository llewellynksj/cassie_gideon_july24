from django.contrib import admin
from .models import Appointment, AvailableDate, AvailableTimeSlot

admin.site.register(Appointment)
admin.site.register(AvailableDate)
admin.site.register(AvailableTimeSlot)
