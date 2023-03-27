
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Starting URL
url = 'http://py4e-data.dr-chuck.net/known_by_Nihal.html'

for i in range(7):
    # Retrieve all of the anchor tags
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')

    # Follow link at position 18
    url = tags[17].get('href', None)

# Last name retrieved
last_name = tags[17].contents[0]
print(last_name)
