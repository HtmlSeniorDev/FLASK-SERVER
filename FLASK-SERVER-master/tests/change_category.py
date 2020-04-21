import requests

url = 'http://127.0.0.1:5000/room/rooms/update/'
data = ({'admin_id': '5c9a61470a975a14c67bcedb', 'category_id': '5c9a60fd0a975a14c67bcd7c', 'change_name': 'Россия',
         'mask': 23})
res = requests.post(url, json=data)

print(res.text)
