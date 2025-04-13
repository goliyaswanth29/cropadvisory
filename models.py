from django.db import models

class Crop(models.Model):
    name = models.CharField(max_length=100)
    optimal_temperature = models.FloatField()
    optimal_rainfall = models.FloatField()
    soil_type = models.CharField(max_length=100)
    season = models.CharField(max_length=20, default="Rabi") 
    def __str__(self):
        return self.name

class WeatherForecast(models.Model):
    date = models.DateField()
    temperature = models.FloatField()
    rainfall = models.FloatField()
    alert = models.TextField(blank=True)

class PestWarning(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    warning = models.TextField()
    date_issued = models.DateField(auto_now_add=True)

