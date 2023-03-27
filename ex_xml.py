import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = 'http://py4e-data.dr-chuck.net/comments_1770981.xml'


data = urllib.request.urlopen(url).read()

tree = ET.fromstring(data)

counts = tree.findall('.//count')

total = 0
for count in counts:
    total += int(count.text)

print(total)
