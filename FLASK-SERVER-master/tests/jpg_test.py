import requests
data = open('2.jpg', 'a')
headers = {'content-type': 'audio/ogg'}
r = requests.post('http://localhost:5000/add/audio', data=data, headers=headers)

print(r)
print(r.text)
#http://localhost:5000/add/audio
#http://httpbin.org/post