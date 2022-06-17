import urllib
from urllib.request import urlopen

url = "http://www.baidu.com"
respose = urlopen(url)

# print(respose.read())

with open("index.html",'w',encoding="utf-8") as fp:
    fp.write(str(respose.read()))

