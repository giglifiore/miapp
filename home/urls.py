from django.urls import path
from . import views

urlpatterns = [
    path('', views.test, name='test'),  # Mostrará el mensaje en la página principal
]
