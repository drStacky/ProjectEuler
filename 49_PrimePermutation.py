'''
Created on Dec 26, 2016


The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, 
and, (ii) each of the 4-digit numbers are permutations of one another.
There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.
What 12-digit number do you form by concatenating the three terms in this sequence?


@author: mstackpo
'''

from datetime import datetime
start = datetime.now()

from euler import sieve, is_prime
from itertools import permutations

n = 10000

for p in sieve(n):
    for y_string in permutations(str(p)):
        x = int(''.join(y_string))
        z = p + 2*(x-p)
        if p > 1000 and is_prime(x) and x > p and is_prime(z):
            my_perms = map( ''.join, permutations( str(p) ) )
            if str(z) in my_perms:
                print(p, x, z)                                      # Finds the answer twice for some reason

end = datetime.now()
print( "runtime = %s" % (end - start) )