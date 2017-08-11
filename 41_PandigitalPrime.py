'''
Created on Dec 14, 2016

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit
pandigital and is also prime.
What is the largest n-digit pandigital prime that exists?

@author: mstackpo
'''

from datetime import datetime
start = datetime.now()

import euler

M = 0

for n in range(1,10):
    pan = euler.get_perms(n)
    M = max(int(p) if euler.is_prime(int(p)) else M for p in pan)

print(M)

end = datetime.now()
print( "runtime = %s" % (end - start) )