'''
Created on Dec 10, 2016

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
(Please note that the palindromic number, in either base, may not include leading zeros.)

@author: mstackpo
'''
from datetime import datetime
start = datetime.now()

sum = 0

# x[::-1] reverses the order of a string x
# bin(i) converts i to binary, but it includes '0b' at start of string that needs to be removed
for i in range(1,1000000):
    if( str(i) == str(i)[::-1] and bin(i)[2:] == (bin(i)[2:])[::-1] ):
        sum += i
print(sum)

end = datetime.now()
print( "runtime = %s" % (end - start) )