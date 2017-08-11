'''
Created on Dec 19, 2016

It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
9 = 7 + 2x1^2
15 = 7 + 2x2^2
21 = 3 + 2x3^2
25 = 7 + 2x3^2
27 = 19 + 2x2^2
33 = 31 + 2x1^2
It turns out that the conjecture was false.
What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

@author: mstackpo
'''

from datetime import datetime
start = datetime.now()

from euler import sieve
from numpy import sqrt
'''
def squares(n):
    for i in range(1,n+1):
        yield i*i
'''
n = 6000
my_sieve = list(sieve(n))

for p in range(9,n+1,2):
    square = True
    for p in my_sieve:
        if p - p >= 2 and p not in my_sieve:
            square = False
            my_num = sqrt( (p - p)/2 )
            if my_num.is_integer():
                square = True
                break
    if not square: print('Not square: ', p)

end = datetime.now()
print( "runtime = %s" % (end - start) )