from math import *
def main():
	divisors = 0
	incrementTriangle = 1
	trianglenumber = 1

	while True:
		divisors = noofdivisors(trianglenumber)
		if divisors<500:
			incrementTriangle+=1
			trianglenumber+=incrementTriangle
		elif divisors>=500:
			print(trianglenumber)
			return 0	
	


def noofdivisors(num):
	noOfdivisors = 0
	intsqrt = int(sqrt(num))
	if sqrt(num) == intsqrt:
		noOfdivisors+=1

	for i in range(1, intsqrt-1):
		if num%i==0:
			noOfdivisors+=2
	return noOfdivisors

main()	