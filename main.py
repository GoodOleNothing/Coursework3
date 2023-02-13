import json
from Class import *

with open('Operations.json') as raw_data:
    operations = json.loads(raw_data)

print(operations)
