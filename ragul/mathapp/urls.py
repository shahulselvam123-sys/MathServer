from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculate_power, name='calculate_power'),
]

