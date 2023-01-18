from django.shortcuts import redirect, render
import requests
import datetime
from django.contrib import messages

# Create your views here.


def home(request):
    city = request.POST.get('city','mohali')
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=bdc8e6c9421ec0c61fda8c49bb4b47ab"
    data = requests.get(url).json()

    if city is " ":
        url = f"https://api.openweathermap.org/data/2.5/weather?q=mohali&appid=bdc8e6c9421ec0c61fda8c49bb4b47ab"

    elif data['cod'] == "404":
        messages.info(request, 'NOT FOUND.')
        return redirect('home')
    else:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=bdc8e6c9421ec0c61fda8c49bb4b47ab"
    data = requests.get(url).json()

    payload = {
        'name': data['name'],
        'weather': data['weather'][0]['main'],
        'description':data['weather'][0]['description'],
        'country':data['sys']['country'],
        'icon': data['weather'][0]['icon'],
        'kel_temperature': int(((data['main']['temp']) - 273) * 9/5 + 32),
        'cel_temperature': int(data['main']['temp']) - 273,
        'pressure': data['main']['pressure'],
        'humidity': data['main']['humidity'],
        'wind':data['wind']['speed'],
        't': datetime.datetime.now()
    }

    context = {'data':payload}
    return render(request, 'home.html',context)