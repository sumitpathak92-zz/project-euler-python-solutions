import math
def paths(n):
	return math.factorial(n)/math.factorial(n/2)/math.factorial(n/2)

print(paths(40))	