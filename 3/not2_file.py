>>> fhand = open("mbox-short.txt")
>>> inp = fhand.read() #Read whole file...
>>> print(len(inp))    #(new lines and all)...
94626                  #into a single string.
>>> print(inp[:20])
From stephen.marquar
+++
fhand = open("mbox-short.txt")
for line in fhand:
    if line.startswith('From:'):
        print(line)
-----

fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip() #gereksiz boşlukları ve karakterleri temzile
    if not '@uct.ac.za' in line:
        continue
    print(line)

-----

fname = input('Enter the file name:')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()
count = 0
for line in fhand:
    if line.startswith('Subject:') :
        count = count + 1
print('There were', count, "subjet lines in", fname)
