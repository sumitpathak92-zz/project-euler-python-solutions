import math
l1=[]
l2=[]
#count = 0
#main_count = 0

def is_prime(n):
    if n == 2:
        return True
    if n%2 == 0 or n <= 1:
        return False
    sqr = int(math.sqrt(n)) + 1
    for divisor in range(3, sqr, 2):
        if n%divisor == 0:
            return False
    return True

def check_left(i):
	x=list(str(i))
	for n in range(1, len(x)):
		y=x[n:]
		s=int(''.join(y))
		if is_prime(s):
			continue
		else:
			return False
	return True
	
def check_right(i):
	x=list(str(i))
	for n in range(1, len(x)):
		y=x[:(-n)]
		s=int(''.join(y))
		if is_prime(s):
			continue
		else:
			return False
	return True						


def truncatable():
	l=[]
	for i in range(10, 1000000):
		if(is_prime(i)):
			if (check_left(i)==True and check_right(i)==True):
				l.append(i)
			else:
				continue
		else:
			continue
	print(sum(l))					


if __name__=='__main__':
	truncatable()