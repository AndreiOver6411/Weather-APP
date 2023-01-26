from django.shortcuts import render
import requests
from .models import City
from .forms import CityFORM

def index3(request):
    appid = "c9e785cb77daa235a547dc4aca5d7dcd"
    url="https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid="+appid

    if(request.method == "POST"):
        form = CityFORM(request.POST)
        form.save()
    form = CityFORM

    all_cities = []

    cities = City.objects.all()
    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'feels_like': res["main"]["feels_like"],
            'humidity': res["main"]["humidity"],
            'speed': res["wind"]["speed"],
            'pressure': res["main"]["pressure"],
            'icon': res["weather"][0]["icon"],
            'deg': res["wind"]["deg"],
        }
        all_cities.append(city_info)

    context = {'all_info':all_cities,'form':form}

    return render(request, 'weather/index3.html',context)

