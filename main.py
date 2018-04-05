import requests
import json

key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJjZTY1ZmMxMC0xYTM0LTAxMzYtZWFhMi0wMzMxODI1NzdmN2YiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTIyODQ2Mjg0LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6ImhhcHAiLCJzY29wZSI6ImNvbW11bml0eSIsImxpbWl0IjoxMH0.bu8aWf0kVn9b0cczYiF4YwVBsHDWWiIrVtgZx0ikcHQ"
url = 'https://api.playbattlegrounds.com/shards/pc-eu/players/'
idBoc = "account.fdddd9dfa3954ad78458e9e9c1172bbb"
iid = "account.d0e19381ceea42a6bd59497fac789943"
headers = {"accept": "application/vnd.api+json",
           "Authorization": "Bearer " + key}

r = requests.get(url+iid, headers=headers)
data = json.loads(r.text)
print json.dumps(json.loads(r.text), indent=4)

print len(data["data"]["relationships"]["matches"]["data"])

