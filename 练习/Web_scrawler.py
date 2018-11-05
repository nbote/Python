from bs4 import BeautifulSoup
import requests

html = requests.get('https://baidu.com').content
soup = BeautifulSoup(html, 'html.parser')
links = soup.find_all('a')

for link in links:
    print(link.string)