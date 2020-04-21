import requests

url = 'http://127.0.0.1:5000/Avatar/buy/'
data = ({
	"user_id":"5e95efa4e675d4fc22611867",
	"avatar_id":"5e73719de675d4fc22611205",
	"price" : 1})
res = requests.post(url, json=data)

print(res.text)
