import requests
import json

TOKEN = "YOUR TOKEN"


# Translate the given address to a coordinate: (lat,lon)
def getCoordinates(address):
    res = requests.get("https://eu1.locationiq.com/v1/search.php?key="+TOKEN+"&q="+address+"&format=json")
    if res.status_code == 200:
        data = json.loads(res.content)
        return (data[0]['lat'],data[0]['lon'])
    else:
        raise Exception("Request Failed, code:"+str(res.status_code))
