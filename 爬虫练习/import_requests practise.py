import requests

text = requests.get('http://www.baidu.com')

print(text.content)
