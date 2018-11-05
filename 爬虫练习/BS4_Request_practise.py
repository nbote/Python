from bs4 import BeautifulSoup
import requests

baidu = requests.get('https://www.baidu.com').content

soup = BeautifulSoup(baidu, 'html.parser')

# print(soup.text)

links = soup.findAll('a')

for link in links:
    print(link.string)

