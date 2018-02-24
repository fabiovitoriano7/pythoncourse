

import urllib2
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://dictionary.cambridge.org/pt/dicionario/ingles/car#dataset-american-english'
html = urllib2.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('span')
line = ''
for tag in tags:
    line = str (tag)
    if line.startswith ('<span class="uk"><span') == True :
        print ("comeco")
        print tag
        print ("FIM")

"""
sum = 0
for tag in tags:
    sum = sum + int(tag.string)
print sum

"""
