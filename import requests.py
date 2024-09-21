import requests
import kivy

localHost='http://172.31.1.203:3000'
r = requests.get(localHost)
print(r.text)

r=requests.post(localHost+"/login", data = {"username":"123", "password": "222"})
print(r.text)