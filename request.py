import requests
import base64

image_path = 'panda.ppm'
with open(image_path, "rb") as img:
    encoded_string = base64.b64encode(img.read())

payload = {'file': encoded_string}
requests.get('http://127.0.0.1:5000/')

r = requests.get('http://127.0.0.1:5000/image', params=payload)