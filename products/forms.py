from django.contrib.auth.models import User
from django import forms
from .models import Theme

theme_choices = Theme.objects.all().values_list('theme', 'theme')
choice_themes = []
for item in theme_choices:
    choice_themes.append(item)
