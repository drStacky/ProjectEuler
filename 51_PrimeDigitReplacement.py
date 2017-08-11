'''
Created on Dec 27, 2016

By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated 
numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the 
smallest prime with this property.
Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

@author: mstackpo
'''

from datetime import datetime
start = datetime.now()

from euler import next_prime, is_prime

prime = next_prime()
p = next(prime)

max_count = 0
max_p = 0
max_p_set = set({})

while p < 100000:
    p = next(prime)

while max_count < 8:
    p = str(next(prime))
    if int(p) not in max_p_set and len(set(p)) < len(p):                # Check for repeated digits
        for i in range(0,len(p)):
            if [digit for digit in p].count(p[i]) > 1:                  # If digit appears more than once
                p_set = set({})                                         # Counts the number of primes made by replacing digits
                for j in range(0,10):
                    z = int(p.replace(p[i],str(j)))
                    if z < int(p): break
                    if is_prime(z):
                        p_set.add(z)
                p_count = 0
                # For the numbers made by replacing digits, if the number is prime, add to the count
                # Funny case: p = 113, we do not want to count 003 = 3, hence the check for number of digits
                for num in p_set:
                    if len(str(num)) == len(p) and is_prime(num): p_count += 1
        if max_count < p_count:
            max_count = p_count
            max_p = p
            max_p_set = p_set
            print(max_p_set)
print(p, max_p_set, p_count)

end = datetime.now()
print( "runtime = %s" % (end - start) )