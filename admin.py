from django.contrib import admin
from .models import Crop, WeatherForecast, PestWarning

admin.site.register(Crop)
admin.site.register(WeatherForecast)
admin.site.register(PestWarning)
