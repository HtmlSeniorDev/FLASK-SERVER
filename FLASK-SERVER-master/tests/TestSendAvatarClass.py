import requests

url = 'http://localhost:5000/friend'
data = ({
    "user": "5ebd949da2c26cbd74c9a75c",
    "friend": "5eb305bcd0645ca462be09c5",

 })
res = requests.post(url, json=data)

print(res.text)
