import json
import requests
#from datetime import datetime
from Class import *

response = requests.get('https://api.npoint.io/e6729ddf2b5e8c56e84a')
operations = json.loads(response.text)
#print(operations)

#datetest = datetime.now()
#format = "%d.%m.%Y"
#print(datetest.strftime(format))

d = Demonstration(operations)
d.looking_for_last_five_executed()
d.collect_and_present_data()

