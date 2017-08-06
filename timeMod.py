import urllib.request, json

def getTime(cidade,lat, lon):
	url = 'http://api.timezonedb.com/v2/get-time-zone?key=GEFOALFQRXCM&format=json&by=position&lat='+lat+'&lng='+lon
	response = urllib.request.urlopen(url)
	data = json.loads(response.read())
	hour = data['formatted']
	answer = 'Hora em '+cidade+':\n'+hour
	return answer

def getCoord(cidade):
	url = 'http://api.openweathermap.org/data/2.5/weather?q='+cidade+'&APPID=f327d9d32e645e5e16acc0129445d355'
	response = urllib.request.urlopen(url)
	data = json.loads(response.read())
	coord = []
	coord.append(str(data['coord']['lat']))
	coord.append(str(data['coord']['lon']))
	answer = getTime(cidade,coord[0],coord[1])
	return answer