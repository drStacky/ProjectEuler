'''
Created on Dec 26, 2016

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?

@author: mstackpo
'''

from datetime import datetime
start = datetime.now()

from euler import next_prime

prime = next_prime()
p = next(prime)
count = 1

while count < 10001:
    count += 1
    p = next(prime)

print(p)

end = datetime.now()
print( "runtime = %s" % (end - start) )

'''
# Print all primes up to a value
while p < 10001:
    print(p)
    p = next(prime)
'''