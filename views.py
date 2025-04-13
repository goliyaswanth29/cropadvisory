from django.shortcuts import render
from .models import Crop, WeatherForecast, PestWarning

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def crops(request):
    crops = Crop.objects.all()
    return render(request, 'crops.html', {'crops': crops})

def crop_suggestions(request):
    crops = Crop.objects.all()
    return render(request, 'crop_suggestions.html', {'crops': crops})

def weather_alerts(request):
    alerts = WeatherForecast.objects.filter(alert__isnull=False)
    return render(request, 'weather_alerts.html', {'alerts': alerts})

def pest_warnings(request):
    warnings = PestWarning.objects.all()
    return render(request, 'pest_warnings.html', {'warnings': warnings})
