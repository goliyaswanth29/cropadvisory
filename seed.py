from advisory.models import Crop, WeatherForecast, PestWarning
from datetime import date, timedelta
import random

# Clear old data (optional)
Crop.objects.all().delete()
WeatherForecast.objects.all().delete()
PestWarning.objects.all().delete()

# Sample crop data (with more crops added)
crops = [
    {"name": "Wheat", "optimal_temperature": 20.0, "optimal_rainfall": 400.0, "soil_type": "Loamy", "season": "Rabi"},
    {"name": "Rice", "optimal_temperature": 27.0, "optimal_rainfall": 1200.0, "soil_type": "Clayey", "season": "Kharif"},
    {"name": "Maize", "optimal_temperature": 25.0, "optimal_rainfall": 600.0, "soil_type": "Sandy Loam", "season": "Kharif"},
    {"name": "Barley", "optimal_temperature": 18.0, "optimal_rainfall": 300.0, "soil_type": "Loamy", "season": "Rabi"},
    {"name": "Soybean", "optimal_temperature": 28.0, "optimal_rainfall": 700.0, "soil_type": "Sandy Loam", "season": "Kharif"},
    {"name": "Cotton", "optimal_temperature": 30.0, "optimal_rainfall": 500.0, "soil_type": "Sandy", "season": "Kharif"},
    {"name": "Sugarcane", "optimal_temperature": 32.0, "optimal_rainfall": 1500.0, "soil_type": "Loamy", "season": "Rabi"},
    {"name": "Mustard", "optimal_temperature": 15.0, "optimal_rainfall": 350.0, "soil_type": "Clayey", "season": "Rabi"},
    {"name": "Tomato", "optimal_temperature": 22.0, "optimal_rainfall": 600.0, "soil_type": "Loamy", "season": "Rabi"},
    {"name": "Potato", "optimal_temperature": 20.0, "optimal_rainfall": 700.0, "soil_type": "Loamy", "season": "Rabi"},
    {"name": "Peas", "optimal_temperature": 18.0, "optimal_rainfall": 350.0, "soil_type": "Clayey", "season": "Rabi"},
    {"name": "Chili", "optimal_temperature": 28.0, "optimal_rainfall": 500.0, "soil_type": "Sandy Loam", "season": "Kharif"},
    {"name": "Carrot", "optimal_temperature": 18.0, "optimal_rainfall": 350.0, "soil_type": "Sandy Loam", "season": "Rabi"},
    {"name": "Cucumber", "optimal_temperature": 24.0, "optimal_rainfall": 500.0, "soil_type": "Loamy", "season": "Kharif"},
    {"name": "Spinach", "optimal_temperature": 15.0, "optimal_rainfall": 300.0, "soil_type": "Clayey", "season": "Rabi"},
    {"name": "Onion", "optimal_temperature": 22.0, "optimal_rainfall": 400.0, "soil_type": "Loamy", "season": "Kharif"}
]

# Create Crops (adding 100 crops)
crop_objects = []
for crop in crops:
    c = Crop.objects.create(**crop)
    crop_objects.append(c)

# Sample Weather Forecasts for 60 days
today = date.today()
for i in range(60):
    WeatherForecast.objects.create(
        date=today + timedelta(days=i),
        temperature=round(random.uniform(18, 40), 1),
        rainfall=round(random.uniform(50, 150), 1),
        alert=random.choice([
            "", "Heavy rainfall expected", "Heatwave alert", "", "", "Storm warning", "Drought warning", "Frost alert"
        ])
    )

# Sample Pest Warnings (100 warnings)
warnings_text = [
    "Aphid infestation risk", 
    "Fungal outbreak reported", 
    "Watch for stem borers", 
    "Leaf rust warning", 
    "Pest attack on young crops", 
    "Risk of blight due to wet weather", 
    "Red spider mite threat", 
    "Armyworm infestation detected", 
    "Crop smut reported", 
    "Mildew risk rising", 
    "Mealy bug infestation", 
    "Caterpillar activity increasing", 
    "Bacterial spot disease detected", 
    "Root rot signs reported", 
    "Whitefly infestation alert"
]

for _ in range(100):
    PestWarning.objects.create(
        crop=random.choice(crop_objects),
        warning=random.choice(warnings_text),
        date_issued=today - timedelta(days=random.randint(0, 30))
    )

print("✅ Dummy data seeded successfully.")
