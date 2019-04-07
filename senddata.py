import requests

ESUSERNAME = "yOUR ELASTIC USERNAME"
ESPASSWORD = "YOUR ELASTIC PASSWORD"

INDEX = "car_monitoring_index"
TYPE = "_doc"
PORT = "9243"
HOST = "YOUR ELASTIC HOST"

headers = {
    'Content-Type': 'application/json',
}

# Send data to kibana
def send_data(id,data):
    url = "https://"+ESUSERNAME+":"+ESPASSWORD+"@"+HOST+":"+PORT+"/"+INDEX+"/"+TYPE+"/"+str(id)
    res = requests.put(url, headers=headers, data=data)
