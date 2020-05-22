hrs = input("Çalışılan Saat:")
try:
    fhrs = float(hrs)
except:
    print("Hata: Lütfen saati rakam olarak giriniz!")
    quit()
rate = input("Saatik Ücret:")
try:
    frate = float(rate)
except:
    print("Lütfen ücreti rakam olarak giriniz!")
    quit()
if fhrs > 40 :
    normalp = fhrs * frate
    overp = (fhrs - 40) * (frate * 0.5)
    payit = overp + normalp
else:
    payit = fhrs * frate
print("Haftalık Yövme: ",payit, "TL", sep='')
