import requests
import pprint

country_code = "in"

url = f"http://api.worldbank.org/v2/country/{country_code}?format=json"

raw_data = requests.get(url)

data = raw_data.json()

print(type(data))
# OUTPUT:
# <class 'list'>

pprint.pprint(data)
# OUTPUT:
"""
[{'page': 1, 'pages': 1, 'per_page': '50', 'total': 1},
 [{'adminregion': {'id': '', 'iso2code': '', 'value': ''},
   'capitalCity': 'London',
   'id': 'GBR',
   'incomeLevel': {'id': 'HIC', 'iso2code': 'XD', 'value': 'High income'},
   'iso2Code': 'GB',
   'latitude': '51.5002',
   'lendingType': {'id': 'LNX', 'iso2code': 'XX', 'value': 'Not classified'},
   'longitude': '-0.126236',
   'name': 'United Kingdom',
   'region': {'id': 'ECS',
              'iso2code': 'Z7',
              'value': 'Europe & Central Asia'}}]]

"""