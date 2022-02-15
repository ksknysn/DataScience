import requests
url = "https://www.sahibinden.com/volkswagen-passat/otomatik?pagingOffset=40"
print("r")
r = requests.get(url, allow_redirects=True)
print("opening")
open('sahibinden2', 'wb').write(r.content)