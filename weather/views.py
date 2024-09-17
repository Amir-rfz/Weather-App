from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=5da0586fb8d75210eacc6848951adb71').read()
        jsonData = json.loads(res)
        data = {
            "country_code":str(jsonData['sys']['country']),
            "coordinate": str(jsonData['coord']['lon']) + ' ' +
            str(jsonData['coord']['lat']),
            "temp": str(jsonData['main']['temp']) + 'k',
            "pressure": str(jsonData['main']['pressure']),
            "humidity": str(jsonData['main']['humidity']),
        } 
    else:
        data = {}
        city = ''
    return render(request,'index.html',{'city' : city,'data' : data})