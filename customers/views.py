from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import RegisterForm, EditProfileForm, PasswordUpdateForm, CreateProfileForm
from django.contrib.auth.models import User
from .models import Theme, Customer


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordUpdateForm
    success_url = reverse_lazy('profile')


class UserRegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')


class UserProfileView(generic.ListView):
    model = Customer
    template_name = 'profile.html'

    # code from Codemy 'Create a Blog Profile Page' Video: http://bit.ly/3OsUgy8:
    def get_context_data(self, *args, **kwargs):
        context = super(UserProfileView, self).get_context_data(*args, **kwargs)
        profile_user = get_object_or_404(Customer, id=self.kwargs['pk'])
        context['profile_user'] = profile_user
        return context


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/settings.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


class UpdateProfileView(generic.UpdateView):
    model = Customer
    template_name = 'update_profile.html'
    fields = ['profile_pic', 'date_of_wedding', 'website_url']

    def get_success_url(self) -> str:
        return reverse_lazy('profile', kwargs={'pk': self.object.pk})


class CreateProfileView(generic.CreateView):
    model = Customer
    form_class = CreateProfileForm
    template_name = 'create_profile.html'

    # Makes the user id available to be able to be saved to the form
    # Code from Codemy 'Profile Account Creation - Django Blog #32' video:
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        return reverse_lazy('profile', kwargs={'pk': self.object.pk})
