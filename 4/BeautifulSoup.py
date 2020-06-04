import urllib.request
import re
from bs4 import BeautifulSoup

url=input('Enter - ')

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

sum=0
count=0

tags = soup('span')
for tag in tags:
    y=str(tag)
    number= re.findall("[0-9]+",y)
    for numbers in number:
        count=count +1
        numbers=int(numbers)
        sum=sum+numbers
print(count)
print(sum)
