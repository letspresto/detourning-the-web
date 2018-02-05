
# coding: utf-8

# In[ ]:

## get modern love list version 1 = using href to do a regular expression
import re
import requests
from bs4 import BeautifulSoup
import sys

url = "http://ben.koski.us/nyt/modern-love"
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'lxml')

links = soup.select('a', href=re.compile('https://www.nytimes'))

# f = open('modern_love_headlines.txt', 'w')

for link in links:
    print link.text.encode('utf-8'), 
#     f.write(link.text.encode('utf-8'))

# f.close()


# In[ ]:

## get modern love list version 2 - using target to find the element
import re
import requests
from bs4 import BeautifulSoup
from sys import stdout as s

url = "http://ben.koski.us/nyt/modern-love"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'lxml')
links = soup.find_all('a', target='_blank')

# f = open('modern_love_headlines.txt', 'w')

for link in links:
    print link.text.encode('utf-8')
#     f.write(link.text.encode('utf-8'))

# f.close()

