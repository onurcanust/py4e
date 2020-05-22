name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count=dict()

for line in handle:
    line=line.rstrip()
    if not line.startswith("From "):
        continue
    else:
        words=line.split()
        mail=words[1]
        count[mail]=count.get(mail,0)+1

x = list(count.values())
y = max(x)

for email, num in count.items():
    if num == y:
        email_id=email

print(email_id,y)
