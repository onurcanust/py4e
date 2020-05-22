rawstr = input("Bir numara giriniz: ")
try:
    ival= int(rawstr)
except:
    ival = -1
if ival > 10:
    prtint("10'dan büyük")
if ival > 10:
    print("10'dan küçük")
if ival == 10:
    print("10'a eşit")
else:
    print("Rakam değil")
