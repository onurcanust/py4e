#http://py4e-data.dr-chuck.net/regex_sum_**.txt
import re

hand = open("regex_sum_**.txt")

sum = 0

for line in hand:
    numbers = re.findall("[0-9]+", line)
    for number in numbers:
        sum = sum + int(number)
print(sum)
