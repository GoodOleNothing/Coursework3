import json
import requests
from demonstration import *

response = requests.get('https://api.npoint.io/e6729ddf2b5e8c56e84a')#Берём данные с внешнего ресурса
operations = json.loads(response.text)


last_five =looking_for_last_five_executed(operations)
collect_and_present_data(last_five)

