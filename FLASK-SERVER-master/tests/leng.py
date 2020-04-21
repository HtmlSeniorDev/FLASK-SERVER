import requests

url = 'http://127.0.0.1:5000/get/notice/'
data = ({'user': '5c9f4f800a975a73eb10b112'})
res = requests.post(url, json=data)

print(res.text)
