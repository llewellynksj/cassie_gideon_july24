from django.urls import path
from .views import UserRegisterView, UserEditView, UserProfileView, PasswordsChangeView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('<int:pk>/profile/', UserProfileView.as_view(), name='profile'),
    path('settings/', UserEditView.as_view(), name='settings'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change_password.html')),
]
