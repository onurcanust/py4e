import json
import urllib.request as jur

j_url = input("Enter location: ")

data = jur.urlopen(j_url).read().decode()
print('Retrieving', j_url)
print('Retrieved', len(data), 'characters')

info = json.loads(data)



print('User count:', len(info))

sum=0
total=0


for comment in info["comments"]:
     sum = sum + int(comment["count"])
     total = total + 1

print('Count:', total)
print('Sum:', sum)
