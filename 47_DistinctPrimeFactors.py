'''
Created on Dec 21, 2016

The first two consecutive numbers to have two distinct prime factors are:
14 = 2 p 7
15 = 3 p 5
The first three consecutive numbers to have three distinct prime factors are:
644 = 2^2 p 7 p 23
645 = 3 p 5 p 43
646 = 2 p 17 p 19.
Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

@author: mstackpo
'''

from datetime import datetime
start = datetime.now()

from euler import prime_factors

found = False
p = 1

# Inefficient because it computes the prime factorization of each number 4 times, but still fast.
while not found:
    if ( len(set(prime_factors(p))) == 4
        and len(set(prime_factors(p+1))) == 4
        and len(set(prime_factors(p+2))) == 4
        and len(set(prime_factors(p+3))) == 4 ):
            print(p, p+1, p+2, p+3)
            found = True
    p += 1

end = datetime.now()
print( "runtime = %s" % (end - start) )