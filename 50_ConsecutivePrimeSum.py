'''
Created on Dec 26, 2016



The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.
The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
Which prime, below one-million, can be written as the sum of the most consecutive primes?

@author: mstackpo
'''

from datetime import datetime
start = datetime.now()

from euler import is_prime, sieve

n = 4000
max_len = 0
max_total = 0

for p in sieve(n):
    total = p
    count = 1
    for x in sieve(n):
        if x > p:
            total += x
            count += 1
            if is_prime(total) and total < 1000000:
                if count > max_len:
                    max_len = count
                    max_total = total
                    print(max_total, max_len)

end = datetime.now()
print( "runtime = %s" % (end - start) )