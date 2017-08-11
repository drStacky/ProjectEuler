'''
Created on Dec 24, 2016

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

@author: mstackpo
'''

from datetime import datetime
start = datetime.now()

total = 0

for p in range(1,1000+1):
    total += p**p

print(total % (10**10))

# One line solution: print( str(sum([i**i for i in range(1,1001)]))[-10:] )

end = datetime.now()
print( "runtime = %s" % (end - start) )