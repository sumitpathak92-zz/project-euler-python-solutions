def checkPandigital(string):
	length = len(string)
	if length>=10:
		return False

	for i in range(1, length+1):
		if str(i) not in string:
			return False
	return True		
def giveNineDigPan(a, b):
	numbers = str(a) + str(b) + str(a*b)
	if len(numbers)!=9:
		return False
	return checkPandigital(numbers)	

products = []
for a in xrange(0, 100000):
	for b in xrange(a, 100000):
		if len(str(a*b)+ str(a) + str(b)) >9:
			break
		if giveNineDigPan(a, b):
			products.append(a*b)

print(sum(set(products)))						