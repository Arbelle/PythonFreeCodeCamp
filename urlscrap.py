import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')

#Retrive All the Anchor Tags

tags=soup('a')
for tag in tags:
	print(tag.get('href', None))
