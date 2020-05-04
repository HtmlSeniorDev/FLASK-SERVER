import requests

url = ' http://localhost:5000/add/invisible/'
data = ({
	"id_user": "5ea07e58a21c4078c28f3f20",
	"id_admin": "5e5f33c90d3f82984060e4d2"})
res = requests.post(url, json=data)

print(res.text)
