import math
from math import log

number=int(input())
sign=input()
result=0
if sign=="natural":
    result=math.log(number)
else:
    result = math.log(number,int(sign))

print(f"{result:.2f}")

