'''
Created on Dec 29, 2016

There are exactly ten ways of selecting three from five, 12345:
123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
In combinatorics, we use the notation, 5C3 = 10.
In general,
nCr =     
n!
r!(n-r)!
    ,where r <= n, n! = nx(n-1)x...x3x2x1, and 0! = 1.
It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.
How many, not necessarily distinct, values of  nCr, for 1 <= n <= 100, are greater than one-million?

@author: mstackpo
'''

from datetime import datetime
start = datetime.now()

from math import factorial

total = 0

for r in range(1,101):
    for n in range(r,101):
        if factorial(n)/factorial(r)/factorial(n-r) > 1000000: total += 1

print(total)

end = datetime.now()
print( "runtime = %s" % (end - start) )