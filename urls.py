from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('crops/', views.crops, name='crops'),
    path('crop-suggestions/', views.crop_suggestions, name='crop_suggestions'),
    path('weather-alerts/', views.weather_alerts, name='weather_alerts'),
    path('pest-warnings/', views.pest_warnings, name='pest_warnings'),
]
