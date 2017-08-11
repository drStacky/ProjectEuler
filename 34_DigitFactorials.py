'''
Created on Dec 5, 2016

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
Find the sum of all numbers which are equal to the sum of the factorial of their digits.
Note: as 1! = 1 and 2! = 2 are not sums they are not included.

@author: mstackpo
'''

'''
9! = 362880
9! * 7 = 2540160 < 9,999,999
So 9,999,999 is an upper bound on the type of numbers we're looking for.
'''

from datetime import datetime
start = datetime.now()

# From ilan on Project Euler - use strings!!!
fact = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
total = 0
for p in range(3,9999999):
    if p==sum( fact[int(d)] for d in str(p) ):
        total += p
print(total)



'''
# Second attempt, much simpler
from math import factorial

Sum = 0
for i in range(10,9999999):
    number = i
    factorial_sum = 0
    while (number != 0 and factorial_sum <= i):
        factorial_sum += factorial(number % 10)
        number //= 10
    if (i == factorial_sum):
        #print(i)
        Sum += i

print( 'Answer: %i' % (Sum) )
'''

'''
# First attempt by brute force
from math import factorial
from timeit import itertools

Sum = 0
for i in range(1,9):
    for j,k in itertools.product(range(0,9), repeat=2):
        num = 100*i + 10*j + k
        if ( factorial(i) + factorial(j) + factorial(k) == num):
            #print( "%i, %i, %i: %i" %(i,j,k, num) )
            Sum += num

for i in range(1,9):  
    for j,k,l in itertools.product(range(0,9), repeat=3):
        num = 1000*i + 100*j + 10*k + l
        if ( factorial(i) + factorial(j) + factorial(k) + factorial(l) == num):
            #print( "%i, %i, %i, %i: %i" %(i,j,k,l, num) )
            Sum += num

for i in range(1,9):
    for j,k,l,m in itertools.product(range(0,9), repeat=4):
        num = 10000*i + 1000*j + 100*k + 10*l + m
        if ( factorial(i) + factorial(j) + factorial(k) + factorial(l) + factorial(m) == num):
            #print( "%i, %i, %i, %i, %i: %i" %(i,j,k,l,m, num) )
            Sum += num

for i in range(1,9):
    for j,k,l,m,p in itertools.product(range(0,9), repeat=5):
        num = 100000*i + 10000*j + 1000*k + 100*l + 10*m + p
        if ( factorial(i) + factorial(j) + factorial(k) + factorial(l) + factorial(m) == num):
            #print( "%i, %i, %i, %i, %i, %i: %i" %(i,j,k,l,m,p, num) )
            Sum += num

print( 'Answer: %i' % (Sum) )
'''


end = datetime.now()
print( "runtime = %s" % (end - start) )