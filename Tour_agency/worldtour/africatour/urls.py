from django.urls import path
from . import views

urlpatterns = [
    path('', views.afritour1, name='africa_tours'),
]