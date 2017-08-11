'''
Created on Dec 12, 2016

Take the number 192 and multiply it by each of 1, 2, and 3:

    192 x 1 = 192
    192 x 2 = 384
    192 x 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)
The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the 
concatenated product of 9 and (1,2,3,4,5). What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated 
product of an integer with (1,2, ... , p) where p > 1?

@author: mstackpo
'''

'''
Obvious (not least) upper bound of 987654321. Anything with 5 digits or more will yield at least a 10 digit number when
using (1,2), which is too big, so a better bound is 9999.
'''
from datetime import datetime
start = datetime.now()

pan = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
max_pan_mult = ''
max_concat = ''

def digit_not_in(m,p):
    return not (str(m) in str(p))

for num in range(1,9999):
    # This 'if' statement was to optimize the runtime before I found a smaller bound
    #if(num%10 != 0 and num%11 != 0 and digit_not_in(5,num)):
        concat_prod = ''
        j = 0
        while(len(concat_prod) < 9):
            j += 1
            concat_prod += str(num*j)
        if(len(concat_prod) == 9 and sorted(concat_prod) == pan and j>1):
            max_pan_mult = num
            max_concat = concat_prod

print(max_pan_mult, max_concat)

end = datetime.now()
print( "runtime = %s" % (end - start) )