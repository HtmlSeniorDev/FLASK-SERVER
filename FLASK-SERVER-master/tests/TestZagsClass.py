import requests

url = 'http://localhost:5000/sending/zags/request/decline/'
data = ({'user_from': '5c9a61470a975a14c67bcedb', 'user_request':'5c9a5db50a975a14c67bbd0c'})
res = requests.post(url, json=data)

print(res.text)
