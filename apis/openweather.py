import requests

apikey= "69c7375697b9a9bb48e9cf8d56655a66"
baseUrl= "https://api.openweathermap.org/data/2.5/forecast"
params= {
    "q":"singapore,sg",
    "APPID":apikey
    }

response= requests.get(baseUrl, params= params)
print(response.content)

