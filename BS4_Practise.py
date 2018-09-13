from bs4 import BeautifulSoup

myHtml = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Nbote</title>
</head>
<body>

<h1>My first HTML text. Good for work!</h1>
<h1> 2nd tag! </h1>
<p>Try harder!!</p>

</body>
</html>'''

jiexi = BeautifulSoup(myHtml, 'html.parser')

jiexi1 = jiexi.findAll('h1')

for i in jiexi1:
    if 'My' in i.string:
        print(i.string)


