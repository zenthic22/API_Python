import requests

r = requests.get("https://dog.ceo/api/breeds/image/random")
print(r.json())