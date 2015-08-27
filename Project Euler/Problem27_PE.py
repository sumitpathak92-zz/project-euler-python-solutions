import time
 
def primes_xrange(stop):
    primes = [True] * stop
    primes[0], primes[1] = [False] * 2
    for ind, val in enumerate(primes):
        if val is True:
            primes[ind*2::ind] = [False] * (((stop - 1)//ind) - 1)
    return primes
 
start = time.time()
 
P = primes_xrange(751000)
a_max, b_max, c_max = 0, 0, 0
for a in range(-1000,1001):
    for b in range(1,1001):
        if P[b] is False: continue
        if b < -1600-40*a or b < c_max: continue
        c, n = 0, 0
        while P[n**2 + a*n + b] is True:
            c += 1
            n += 1
        if c > c_max:
            a_max, b_max, c_max = a, b, c
 
prod = a_max * b_max
 
elapsed = time.time() - start
 
print "a=%s, b=%s, longest sequence = %s, prod=%s\nfound in %s seconds"\
% (a_max, b_max, c_max, prod, elapsed)