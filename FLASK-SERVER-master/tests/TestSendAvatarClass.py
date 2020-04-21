import requests

url = ' http://localhost:5000/delete/photo/profile/'
data = ({
	"id_nick":"5e95efa4e675d4fc22611867",
	"description":"asdsadsa",
	"photo_id" : '5e9f418aa606c4daf49b8600'})
res = requests.post(url, json=data)

print(res.text)
