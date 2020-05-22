largest = None
smallest = None

while True:
    inp = input("Enter a number: ")
    if inp == "done" :
        break
    try:
        num = float(inp)
    except:
        print ("Invalid input")
        continue
    if smallest is None:
        smallest = num
        largest = num
    if num > largest :
        largest = num
    elif num < smallest :
        smallest = num

def done(largest,smallest):
    print ("Maximum is", int(largest))
    print ("Minimum is", int(smallest))

done(largest,smallest)
