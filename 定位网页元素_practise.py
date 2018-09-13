import requests

from bs4 import BeautifulSoup

data=requests.get('https://www.google.com').content

soup=BeautifulSoup(data,'html.parser')

print(soup.body.div.attrs)



