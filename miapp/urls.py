from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),  # redirige la URL base a la app "home"
    path('admin/', admin.site.urls),
]
