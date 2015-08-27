def properDivisors(n):
	list=[]
	for i in range(1, ((n/2)+1)):
		if n%i == 0:
			list.append(i)
	return list
	
def total(x):
	total = sum(x)
	return total


def main():
	tally = 0
	for i in range(1, 10001):
		x = properDivisors(i)
		x1 = total(x)
		x3 = properDivisors(x1)
		x4 = total(x3)
		if (i==x4) and (i!=x1):
			tally+=i
	print(tally)

if __name__ == '__main__':
	main()