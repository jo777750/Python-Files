import requests

country_code = "in"

url = f"http://api.worldbank.org/v2/country/{country_code}?format=json"

raw_data = requests.get(url)

print(raw_data.headers)
# OUTPUT (truncated):
# {'Date': 'Fri, 29 Jul 2022 13:35:31 GMT', 'Content-Type': 'application/json;charset=utf-8', ...

print(raw_data.headers['Content-Type'])
# OUTPUT:
# application/json;charset=utf-8

print(raw_data.text)
# OUTPUT (truncated):
# [{"page":1,"pages":1,"per_page":"50","total":1},[{"id":"GBR","iso2Code":"GB","name":"United Kingdom", ...

print(type(raw_data.text))
# OUTPUT:
# <class 'str'>