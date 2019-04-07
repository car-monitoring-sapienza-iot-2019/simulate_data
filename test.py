import datetime
import random
import sys
import json
from numpy.random import normal
from geocoder import getCoordinates
from senddata import send_data
from time import sleep
from tqdm import tqdm

random.seed(datetime.datetime.now())


def generate_data(lat,lon,speed):

  data = '{\
      "date": '+json.dumps(datetime.datetime.now().isoformat())+',\
      "location": {\
        "lat": '+str(lat)+',\
        "lon": '+str(lon)+'\
      },\
      "throttle": 0.0,\
      "rpm": 0.0,\
      "massAirFlow": 0.0,\
      "speed": '+str(speed)+',\
      "engineTemperature": 0.0\
  }'

  return data

# -> Generate geocoords from the given street name and numbers from start to stop
# -> Generate a random values for speed
# -> Send data to kibana at the specified index
def simulate_traffic(address,start,stop,change_mean_each=50,means=[5,10,60,90,130]):

  size = stop-start+1
  speeds_vector = [normal(loc=m, scale=5.0, size=50) for m in means]

  speed_idx = 0
  speeds = speeds_vector[0]
  for i in tqdm(range(size)):
    if speed_idx%(change_mean_each-1) == 0:
      speeds = speeds_vector[random.randint(0,len(means)-1)]
      speed_idx = 0
    (lat,lon) = getCoordinates(address+","+str(start+i))
    speed = speeds[speed_idx] if speeds[speed_idx] > 0 else 0
    data = generate_data(lat,lon,int(speed))
    ID = random.randint(1,sys.maxsize)
    send_data(ID,data)
    sleep(0.1)
    

# Roma, Via Tiburtina, 1-300, 5 km/h
simulate_traffic("Roma, Via Tiburtina",1,300)
# Roma, Via Cassia, 1-400, 90 km/h
simulate_traffic("Roma, Via Cassia",1,400)
# Roma, Via Trionfale,10-200,20 km/h
simulate_traffic("Roma, Via Trionfale",10,200)



