'''
Created on Jan 10, 2017

The number 512 is interesting because it is equal to the sum of its digits raised to some power: 5 + 1 + 2 = 8, and 8^3 = 512.
Another example of a number with this property is 614656 = 28^4.
We shall define an to be the nth term of this sequence and insist that a number must contain at least two digits to have a sum.
You are given that a2 = 512 and a10 = 614656.
Find a30.

@author: mstackpo
'''

from datetime import datetime
start = datetime.now()

from euler import sum_digits   

pows = set()
for base in range(2,100):
    for exp in range(2,20):
        x = base**exp
        s = sum_digits(x)
        if x > 10 and s == base:
            pows.add(x)

print(sorted(pows)[29])

end = datetime.now()
print( "runtime = %s" % (end - start) )