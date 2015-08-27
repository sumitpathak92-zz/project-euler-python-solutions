def fibR(n):
	a, b = 1, 1
	for i in range(n-1):
		a, b = b, a+b
	return a
	
def memoize(fn, arg):
	memo= {}
	if arg not in memo:
		memo[arg] = fn(arg)
	return str(memo[arg])	


result = [0,0]
i=1
while True:
	fibm = memoize(fibR, i)
	if len(fibm) == 1000:
		#result[0] = fibR(i)
		result[1] = i
		break
	else:
		i+=1

print(result[1])