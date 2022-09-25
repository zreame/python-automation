import requests
import json

lacroix= "0012993441012"
greentea= "073366118238"

def retrieve(item_code) :
    base_url= "https://api.upcitemdb.com/prod/trial/lookup"
    parameters= {"upc" : item_code}
    response= requests.get(base_url, params= parameters)
    
    # json not a native data structure in py, json lib converts json to dictionary
    info = json.loads(response.content)
    # dumps + indent makes json more readable
    # print(json.dumps(info, indent=2))
    name= info["items"][0]["title"]
    merchant= info["items"][0]["offers"][0]["merchant"]
    print(name, merchant)

retrieve(lacroix)