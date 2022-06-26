import requests

respons = requests.get('http://127.0.0.1:3000/api/main')
print(respons.json())
