'''
Created on Dec 29, 2016

It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits

@author: mstackpo
'''

from datetime import datetime
start = datetime.now()

done = False
x = 0

while not done:
    x += 1
    if sorted(list(str(x))) == sorted(list(str(2*x))) \
        == sorted(list(str(3*x))) \
        == sorted(list(str(4*x))) \
        == sorted(list(str(5*x))) \
        == sorted(list(str(6*x))):
            done = True
print(x, 2*x, 3*x, 4*x, 5*x, 6*x)

end = datetime.now()
print( "runtime = %s" % (end - start) )