import urllib.request, json

def getWeather(cidade):
    url = 'http://api.openweathermap.org/data/2.5/weather?q='+cidade+'-&APPID=f327d9d32e645e5e16acc0129445d355'
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    temp = int(data['main']['temp']) - 273.15
    press = str(data['main']['pressure'])
    umid = str(data['main']['humidity'])
    vento = str(int(data['wind']['speed'])*3.6)
    temp = "%.2f"%temp
    temp = str(temp)
    answer = "Clima em "+cidade+":\nTemperatura: "+temp+" C\nUmidade: "+umid+"%\nVento: "+vento+" Km/h\nPressao: "+press+" hPa"
    return answer
