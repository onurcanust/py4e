#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#<  0.6 F
score = input("Enter Score: ")
try:
    fscore = float(score)
except:
    print("Error: Pleae enter a number between 0.0 and 1.0")
    quit()
if 0.0 <= fscore < 0.6:
    print("F")
elif 1.0 >= fscore >= 0.9:
    print("A")
elif 0.9 > fscore >= 0.8:
    print("B")
elif 0.8 > fscore >= 0.7:
    print("C")
elif 0.7 > fscore >= 0.6:
    print("D")
else :
    print("Error: Value out of range")
    
