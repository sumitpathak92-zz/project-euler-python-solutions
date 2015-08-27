import itertools
l = [0,1,2,3,4,5,6,7,8,9]
x = list(itertools.permutations(l))
x.sort()
print(x[999999])