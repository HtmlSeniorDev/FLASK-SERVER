import requests

url = 'http://79.174.12.77:5000/personalrooms/'
data = ({
    "nic_id": "5d5a81b60a975a393998507d",
 })
res = requests.post(url, json=data)

print(res.text)
