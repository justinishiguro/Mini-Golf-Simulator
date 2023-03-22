import requests
import time

url = "http://cpen291-2.ece.ubc.ca/"
data = {"key": "value"}

while True:
    response = requests.post(url, data=data)
    print(response.text)
    time.sleep(2)

