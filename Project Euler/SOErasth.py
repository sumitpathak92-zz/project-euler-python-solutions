####################################################
# THIS IMPLEMENTATION USES SET LOOKUP ##############
####################################################
import math
from collections import deque

count = 0
def sOfErat(n):
	multiples = set()
	for i in range(2, n+1):
		if i not in multiples:
			yield i #to be studied still!
			multiples.update(range(i*i, n+1, i))


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


sOfErat_res = list(sOfErat(1000000))



for i in range(len(sOfErat_res)):
	l1=[]
	prime_count=0
	sOfErat_res[i] = str(sOfErat_res[i])
	sOfErat_res[i] = list(sOfErat_res[i])
	g= deque(sOfErat_res[i])
	for i in range(len(g)):
		l1.append(''.join(k for k in list(g)))
		g.rotate(-1)

	for j in l1:
		if is_prime(int(j)):
			prime_count+=1
		
	if prime_count==len(l1):
		count+=1
print(count)		