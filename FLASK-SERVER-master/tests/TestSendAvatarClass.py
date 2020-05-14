import requests

url = 'http://localhost:5000/avatar/send'
data = ({
    "user": "5ebd63f7a2c26cbd74c9a687",
    "sender": "5ebd5a34a2c26cbd74c9a669",
    "avatar": "5eb6e8a6735e0b0d7289a715"
 })
res = requests.post(url, json=data)

print(res.text)
