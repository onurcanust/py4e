#use romeo.txt file

fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
        print("Error:",fname, "file not exist")
        quit()

lst = list()

for line in fh:
    line.rstrip
    words = line.split()

for word in words:
    if word not in lst :




print(line.rstrip())
