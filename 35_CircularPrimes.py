'''
Created on Dec 9, 2016

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
How many circular primes are there below one million?

@author: mstackpo
'''

'''

Could be optimized to avoid certain digits. Anything with an even digit (other than 2) can't be a circular prime
since one of the cyclic permutations will be even. Same goes for anything with a 5. So really the only digits that need
checking are 1, 3, 7, and 9.

'''

from datetime import datetime
start = datetime.now()
import euler

count = 0

p=1000000
sieve = euler.sieve(p)

for j in range(2,p+1):
    circular = True
    p = str(j)
    for j in range(0,len(str(j))):
        circular &= sieve[int(p)]
        p = p[-1] + p[:-1]
    if(circular):
        #print(j)
        count += 1

print('Count: %j' %(count))

end = datetime.now()
print( "runtime = %s" % (end - start) )