'''
Contains useful functions for Project Euler problems.

Created on Dec 10, 2016

@author: mstackpo
'''
import math, itertools

# Sieve of Eratosthenes
# Returns boolean list where sieve[j] is true if j is prime
'''
# My inefficient version, returns a list
def sieve(p):
    sieve = [True]*(p+1)
    sieve[0] = False
    sieve[1] = False
    bound = math.floor( math.sqrt(p) )
    for j in range(2, bound):
        j = 2*j
        while(j <= p):
            sieve[j] = False
            j += j
    return(sieve)
'''

# Faster sieve found on stackoverflow: http://stackoverflow.com/questions/3939660/sieve-of-eratosthenes-finding-primes-python
# generator function, returns a generator
def sieve(n):
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples:
            yield i
            multiples.update(range(i*i, n+1, i))

# Implementation of generator for problem 41 that was too inefficient
#sieve = euler.sieve(n)
#print( max(p for p in sieve if euler.is_pandigital(p) ) )

# is_prime and get_primes taken from: https://jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/
def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0: 
                return False
        return True
    return False

# returns True if check is a permutation of ref (works on strings and integers)
def is_perm(check, ref):
    return str(check) in map( ''.join, itertools.permutations( str(ref) ) )

def next_prime():
    p = 2
    while(True):
        if is_prime(p):
            yield p
        p += 1

# Used on a list to extract the prime numbers
def get_primes(number):
    while True:
        if is_prime(number):
            yield number
        number += 1

# Checks if p is pandigital using digits up to length of p
def is_pandigital(p):
    n = len(str(p))
    p = []    
    for j in range(0,n):
        p.append(str(j+1))
    return p == sorted(str(p))

def get_perms(start, stop = None):
    p = []
    
    if stop == None:
        stop = start
        start = 1
    if stop <= start:
        p.append(str(start))
    else:
        # For every permutation of stop-1, insert stop in between each digit to produce new permutations
        for y_string in get_perms(start, stop-1):
            for j in range(len(y_string)+1):
                p.append(y_string[:j] + str(stop) + y_string[j:])
    # Results is returned as a list of strings
    return p

# Same as above but uses generator, (returns iterator-like object)
def get_perms_gen(start, stop = None):
    if stop == None:
        stop = start
        start = 1
    if stop <= start:
        yield str(start)
    else:
        # For every permutation of stop-1, insert stop in between each digit to produce new permutations
        for y_string in get_perms(start, stop-1):
            for j in range(len(y_string)+1):
                yield y_string[:j] + str(stop) + y_string[j:]

# Returns list of prime factors of n (with repetition)
# Found on Stackoverflow: http://stackoverflow.com/questions/15347174/python-finding-prime-factors
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

# Recursive function that sums the digits of a positive int
def sum_digits(n):
    if n <= 0: return 0
    else:
        return n%10 + sum_digits(n//10)

# Returns generator for numbers that are i^x < n for some integers i and x
# Used in 119
def powers(n):
    pows = set()
    for i in range(2,n+1):
        if i in pows:
            yield i
        pows.update(i**x for x in range(2, int(math.log(n,i)) + 1 ))