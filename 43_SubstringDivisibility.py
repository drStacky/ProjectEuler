'''
Created on Dec 18, 2016

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.
Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.

@author: mstackpo
'''
from datetime import datetime
start = datetime.now()

import euler

total = 0

''' # 14.5 seconds
pan = euler.get_perms_gen(0,9)
for num in pan:
    cond1 = int( num[1:4] )%2 == 0
    cond2 = int( num[2:5] )%3 == 0
    cond3 = int( num[3:6] )%5 == 0
    cond4 = int( num[4:7] )%7 == 0
    cond5 = int( num[5:8] )%11 == 0
    cond6 = int( num[6:9] )%13 == 0
    cond7 = int( num[7:10] )%17 == 0
    if(cond1 and cond2 and cond3 and cond4 and cond5 and cond6 and cond7):
        total += int(num)
'''

# Not as readable, but putting all the conditions together saves time (if first one fails, if statement skipped immediately).
pan = euler.get_perms_gen(0,9)
for num in pan:
    if int( num[1:4] )%2 == 0 and int( num[2:5] )%3 == 0 and int( num[3:6] )%5 == 0 and int( num[4:7] )%7 == 0 and int( num[5:8] )%11 == 0 and int( num[6:9] )%13 == 0 and int( num[7:10] )%17 == 0:
        total += int(num)

print(total)

end = datetime.now()
print( "runtime = %s" % (end - start) )