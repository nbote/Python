from bs4 import BeautifulSoup
import requests

baidu = requests.get('https://github.com').content

soup = BeautifulSoup(baidu, 'html.parser')

# print(soup.text)

links = soup.findAll('title')

for link in links:
    print(link.string)

