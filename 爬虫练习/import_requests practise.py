import requests

# Inty版本

text = requests.get('http://www.baidu.com')

print(text.content)


# 周莫烦版本
# from urllib.request import urlopen
#
# html=urlopen('http://www.baidu.com').read().decode('utf-8')
# print(html)

