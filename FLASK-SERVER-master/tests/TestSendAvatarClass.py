import requests

url = ' http://localhost:5000/set/photo/profile/'
data = ({
	"photo_id": "5eb35c47d0645ca462be0be3",
	"user_id": "5eaf4a1884fbb8f8c0311f1f"})
res = requests.post(url, json=data)

print(res.text)
