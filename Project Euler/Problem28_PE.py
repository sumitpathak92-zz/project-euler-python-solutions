def g(L):
    n = (L-1) // 2
    return (16*n**3 + 30*n**2 + 26*n + 3) // 3
 
L = 1001 
print("Sum of both diagonals of a", L, "square \nspiral =", g(L))

# sod = 1
# l=[] 
# s=[]
# for n in range(3, 1003, 2):
# 	i=n-1
# 	for k in range(0,4):
# 		sod = sod+i
# 		l[k] = sod
# 	s.append(sum(l))