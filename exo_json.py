import urllib.request, urllib.parse, urllib.error
import json

url = 'http://py4e-data.dr-chuck.net/comments_1770982.json'

data = urllib.request.urlopen(url).read()
info = json.loads(data)

total = 0
for comment in info['comments']:
    total = total + comment['count']
print(total)
