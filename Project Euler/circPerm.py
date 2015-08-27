num = str(1234)
num = list(num)
# aux = ''
# res2 = []

# for i in num:
# 	aux = aux.join(i)
# 	num.pop(int(aux))
# 	#res2.append(num.append(aux))
# 	num.append(aux)

# print(num)	

#### Using collections.deque ####
from collections import deque

g= deque(num)
for i in range(len(g)):
	print(''.join(k for k in list(g)))
	g.rotate(-1)

###### without using library functions ########

n = len(num)
res = ([num[i-j] for i in range(n)] for j in range(n, 0, -1))
print(list(res))	