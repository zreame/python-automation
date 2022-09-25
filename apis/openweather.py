import requests

apikey= input("Enter api key: ")
baseUrl= "https://api.openweathermap.org/data/2.5/forecast"
params= {
    "q":"singapore,sg",
    "APPID":apikey
    }

response= requests.get(baseUrl, params= params)
print(response.content)

