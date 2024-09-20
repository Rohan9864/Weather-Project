from django.shortcuts import render
import requests
from django.contrib import messages

# Create your views here.
def index(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city="kathmandu"

    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=ab55324db5a0b973b621c0871d818090"
    params={'units':"metric"}
    try:
        data=requests.get(url,params).json() 
        temp=data['main']["temp"]
        humidity=data['main']["humidity"]
        wind=data['wind']["speed"]
        desc=data['weather'][0]["description"]
        icon=data['weather'][0]["icon"]
        return render(request, 'index.html',{'temp':temp,'city':city,'humidity':humidity,'wind':wind,'desc':desc,'icon':icon})
    except:
        temp=0
        humidity=0
        wind=0
        desc="none"
        icon="none"
        messages.error(request,"City not found!!!")

        return render(request, 'index.html',{'temp':temp,'city':city,'humidity':humidity,'wind':wind,'desc':desc,'icon':icon})
      
    