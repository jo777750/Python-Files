import requests

country_code = "in"

url = f"http://api.worldbank.org/v2/country/{country_code}?format=json"

raw_data = requests.get(url)

data = raw_data.json()

print(type(data))
# OUTPUT:
# <class 'list'>

print(data)
# OUTPUT (truncated):
# [{'page': 1, 'pages': 1, 'per_page': '50', 'total': 1}, [{'id': 'GBR', 'iso2Code': 'GB', ...