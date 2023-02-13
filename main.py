import json
import requests
import datetime
from Class import *

response = requests.get('https://api.npoint.io/e6729ddf2b5e8c56e84a')
operations = json.loads(response.text)
#print(operations)


d = Demonstration(operations)
d.looking_for_last_five_executed()
d.collect_and_place_data()
#print(d.__repr__())
