import requests

URL = 'http://127.0.0.1:8000/outro_recurso'

response = requests.get(URL)

print(response.json())