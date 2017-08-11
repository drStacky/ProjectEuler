'''
Created on Dec 10, 2016

The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, 
and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

@author: mstackpo
'''

from datetime import datetime
start = datetime.now()

import euler

p = 1000000
sieve = euler.sieve(p)
Sum = 0

for p in range(11,p):
    diff = p
    prime = True
    # Strip off digits from right and check for prime
    while(diff > 0 and prime):
        prime &= sieve[diff]
        diff //= 10
    # Strip of digits from left and check for prime
    diff = p
    while(diff > 0 and prime):
        prime &= sieve[diff]
        # convert to string to strip digit off right, special case if diff is single digit
        diff = int(str(diff)[1:]) if diff > 9 else 0 
    if(prime):
        # print(p)
        Sum += p

print(Sum)

end = datetime.now()
print( "runtime = %s" % (end - start) )