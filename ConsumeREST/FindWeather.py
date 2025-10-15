from urllib import request
import json

city=input('Enter city : ')
response=request.urlopen("http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=5ea9269ece0f0c287803a5b69fca4d80")
data=response.read()
info=json.loads(data)

#print(info)

desc=info['weather'][0]['description']
feels=info['main']['feels_like']
feels=feels-272.15

print(f"Weather description : {desc}")
print("Feels like temperature : %.2f celsius" %feels)
