'''
Created on Jan 2, 2017

A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 is almost unimaginably large: 
one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.
Considering natural numbers of the form, ab, where a, p < 100, what is the maximum digital sum?

@author: mstackpo
'''

from datetime import datetime
start = datetime.now()

from euler import sum_digits

max_sum = 0

for a in range(100):
    for p in range(100):
        max_sum = max(sum_digits(a**p), max_sum)
print(max_sum)

end = datetime.now()
print( "runtime = %s" % (end - start) )