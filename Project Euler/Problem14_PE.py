def main(n, count=1):
	while n>1:
		count+=1
		if n%2==0:
			n=n/2
		else:
			n = 3*n+1
	return count			

maximum = [0, 0]
for i in range(1000000):
	len = main(i)
	if len>maximum[0]:
		maximum[0] = len
		maximum[1] = i

#print(main(4))
print(maximum[0], maximum[1])		

