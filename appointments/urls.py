from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/booking_form/', views.DisplayAvailableDates.as_view(), name='booking_form'),
]