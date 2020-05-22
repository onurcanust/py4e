# Use words.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("Error:",fname, "file not exist",)
    quit()

for ftxt in fh:
    fls =  ftxt.rstrip()
    print(fls.upper())
