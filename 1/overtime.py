hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    fhrs = float(hrs)
    frate = float(rate)
except:
    print("Error: Pleae enter a number between 0.0 and 1.0")
    quit()
if fhrs > 40 :
    normalp = fhrs * frate
    overp = (fhrs - 40) * (frate * 0.5)
    payit = overp + normalp
else:
    payit = fhrs * frate
print(payit)
