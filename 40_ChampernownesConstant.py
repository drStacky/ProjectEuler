'''
Created on Dec 14, 2016

An irrational decimal fraction is created by concatenating the positive integers:
0.123456789101112131415161718192021...
It can be seen that the 12th digit of the fractional part is 1.
If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000

@author: mstackpo
'''

from datetime import datetime
start = datetime.now()

champ = ''
for j in range(1,1000000):
    champ += str(j)

product = 1
for j in range(0,6):
    product *= int(champ[10**j - 1])

print(product)


end = datetime.now()
print( "runtime = %s" % (end - start) )