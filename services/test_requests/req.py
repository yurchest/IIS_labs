import requests
import random

params = {'cus_id': 12345}
data = {
    "age":          random.randint(1,80),
    "job":          "housemaid",
    "marital":	    "married",
    "education":	"secondary",
    "default":	    "no",
    "balance":	    random.randint(1000,1000000),
    "housing":	    "yes",
    "loan":	        "no",
    "contact":	    "cellular",
    "day":	        random.randint(1,10),
    "month":	    "aug",
    "duration":     699,
    "campaign":     2
    } 

response = requests.post('http://127.0.0.1:8001/api/prediction', params=params, json=data)
print(response.json())