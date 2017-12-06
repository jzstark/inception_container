import requests
import base64
import json

image_path = 'cat.jpg'
with open(image_path, "rb") as img:
    encoded_string = base64.b64encode(img.read())

payload = {'type':'ppm', 'content': encoded_string}
requests.get('http://127.0.0.1:5000/')

r = requests.get('http://127.0.0.1:5000/image', params=payload)

js_resp = json.loads(json.loads(r.content))

print js_resp
print js_resp[0]
