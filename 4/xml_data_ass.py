import urllib.request as url
import xml.etree.ElementTree as et

address = input('Enter location: ')

total = 0
sum = 0


read = url.urlopen(address).read()
print('Retrieving', address)

tree = et.fromstring(read)

counts = tree.findall('.//count')
for count in counts:
    sum = sum + int(count.text)
    total  = total + 1

print('Count:', total)
print('Sum:', sum)
