import requests

url = 'http://12:5000/sending/zags/request/decline/'
data = ({'nic_id': '5c9a61470a975a14c67bcedb'})
res = requests.post(url, json=data)

print(res.text)
