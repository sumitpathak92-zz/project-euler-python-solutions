def getPrimesBelowN(n=1000000):
	#use seive of erasthones
    from math import ceil
    primes = [True] * n
    primes[0] = False
    primes[1] = False
    primeList = []
    roundUp = lambda n, prime: int(ceil(float(n) / prime))
    for currentPrime in xrange(2, n):
        if not primes[currentPrime]:
            continue
        primeList.append(currentPrime)
        for multiplicant in xrange(2, roundUp(n, currentPrime)):
            primes[multiplicant * currentPrime] = False
    return primes
 
def isCircularPrime(primes, number):
    
    number = str(number)
    for i in xrange(0, len(number)):
        rotatedNumber = number[i:len(number)] + number[0:i]
        if not primes[int(rotatedNumber)]:
            return False
    return True
 
if __name__ == "__main__":
    #print("Start sieving.")
    primes = getPrimesBelowN(1000)
    #print("End sieving.")
    numberOfPrimes = 2
    print(2)    
    print(5)    
    for prime, isPrime in enumerate(primes):
        if (not isPrime) or ("2" in str(prime)) or \
           ("4" in str(prime)) or ("6" in str(prime)) or \
           ("8" in str(prime)) or ("0" in str(prime)) or \
           ("5" in str(prime)):
            continue
        if isCircularPrime(primes, prime):
            print(prime)
            numberOfPrimes += 1
 
    print("Number of circular primes: %i" % numberOfPrimes)