from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
    path('customers/', include('django.contrib.auth.urls')),
    path('customers/', include('customers.urls')),
]
