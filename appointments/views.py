from django.shortcuts import render, get_object_or_404
from .models import Appointment, AvailableDate, AvailableTimeSlot
from customers.models import Customer
from django.views import generic


class DisplayAvailableDates(generic.ListView):
    model = AvailableDate
    template_name = 'booking_form.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DisplayAvailableDates, self).get_context_data(*args, **kwargs)
        profile_user = get_object_or_404(Customer, id=self.kwargs['pk'])
        context['profile_user'] = profile_user
        return context

    def get_success_url(self) -> str:
        return reverse_lazy('profile', kwargs={'pk': self.object.pk})
