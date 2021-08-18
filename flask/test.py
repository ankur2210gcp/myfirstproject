import requests

BASE = "http://127.0.0.1:5000/"
#response = requests.put(BASE + "video/3", {"likes": 10, "name": "tim", "views": 112})
#response = requests.get(BASE + "video/2")
#response = requests.patch(BASE + "video/9", {"likes": 101,"name": "tim", "views": 112})
#response = requests.upsert(BASE + "video/10", {"likes": 102,"name": "tim", "views": 113})
print(response.json())
