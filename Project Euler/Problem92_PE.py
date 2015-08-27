'''
Created on 27-Aug-2015

@author: sumit
'''

def problem92(limit):
    arrive = [None] * limit 
    arrive[1], arrive[89] = 1, 89
    for n in range(2, limit):
        chain = []
        while not arrive[n]:
            chain.append(n)
            n = square_digits(n)
        dest = arrive[n]
        for term in chain:
            arrive[term] = dest
    return arrive.count(89)

def square_digits(n):
    total = 0
    while n:
        total += (n % 10) ** 2
        n //= 10
    return total

#from timeit import timeit
#print#(timeit(lambda:problem92b(10**7), number=1))
print(problem92(10**7))


