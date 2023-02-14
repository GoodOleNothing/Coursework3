import pytest
import json
import requests
from demonstration import *
response = requests.get('https://api.npoint.io/e6729ddf2b5e8c56e84a')#Берём данные с внешнего ресурса
operations = json.loads(response.text)

@pytest.fixture()
def operations():
    return operations

def test_looking_for_last_five_executed():
    assert looking_for_executed(operations) == 22
