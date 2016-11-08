import urllib.request
import json
from pprint import pprint

url = "https://maps.googleapis.com/maps/api/geocode/json?address=Prudential%20Tower"
f = urllib.request.urlopen(url)
response_text = f.read().decode('utf-8')
response_data = json.loads(response_text)
pprint(response_data)