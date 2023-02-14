import json
import requests
from demonstration import *

response = requests.get('https://api.npoint.io/e6729ddf2b5e8c56e84a')#Берём данные с внешнего ресурса
operations = json.loads(response.text)

d = Demonstration(operations) #Создаём экземпляры класса
d.looking_for_last_five_executed()
d.collect_and_present_data()

