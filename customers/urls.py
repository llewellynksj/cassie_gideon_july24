from django.urls import path
from .views import UserRegisterView, UserEditView, UserProfileView, PasswordsChangeView, UpdateProfileView, CreateProfileView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('settings/', UserEditView.as_view(), name='settings'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change_password.html')),
    path('<int:pk>/profile/', UserProfileView.as_view(), name='profile'),
    path('<int:pk>/update_profile/', UpdateProfileView.as_view(), name='update_profile'),
    path('create_profile/', CreateProfileView.as_view(), name='create_profile'),
]
