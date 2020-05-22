# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("Error:",fname, "file not exist")
    quit()

count = 0.0
total = 0.0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    num = float(line[21:])
    total = num + total

avr = total / count

print("Average spam confidence:", avr)
