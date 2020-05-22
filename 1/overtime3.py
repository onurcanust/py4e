def computepay(h,r):
    if h > 40:
        pay = 40*r + (h - 40)*(r*1.5)
        return pay
    else:
        pay = r*h
        return pay
    #return 42.37

hrs = input("Enter Hours:")
rate = input("Enter Rate:")

try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error: Enter a number!")
    quit()

p = computepay(h,r)
print("Pay",p)
