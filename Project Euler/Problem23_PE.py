def check(n):
  s=0
  for i in xrange(1,n/2+1):
    if n%i==0:
      s+=i
  return s>n

l=28123 
sieve=[False]*l 

abundant=[]
for i in xrange(12,l):
  if check(i):
    abundant.append(i)

for i in xrange(len(abundant)): 
  for j in xrange(i,len(abundant)):
    if abundant[i]+abundant[j]<l:
      sieve[abundant[i]+abundant[j]]=True 

print(sum([i for i in xrange(len(sieve)) if not(sieve[i])]))