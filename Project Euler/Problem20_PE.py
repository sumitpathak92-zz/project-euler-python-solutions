import math
fact = math.factorial(100)
fact = str(fact)
sum = 0
for i in fact:
	sum+=int(i)
print(sum)