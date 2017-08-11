'''
Created on Jan 13, 2017

Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each "_" is a single digit.

@author: mstackpo
'''

'''
x^2 = 1_2_3_4_5_6_7_8_9_0
x^2%10 = 0, so x%10 = 0 and x^2%100 = 0

y^2 = 1_2_3_4_5_6_7_8_9
y ends in 3 or 7
'''

from datetime import datetime
start = datetime.now()

def concealed(x):
    y = str(x)
    return y[-15] == '2' and y[-13] == '3' and y[-11] == '4' and y[-9] == '5' \
        and y[-7] == '6' and y[-5] == '7' and y[-3] == '8' and y[-1] == '9'

x = 10**7

while True:
    y1 = x*10 + 3
    y2 = x*10 + 7
    if concealed(y1**2):
        print('This is it', y1*10)
        break
    elif concealed(y2**2):
        print('This is it', y2*10)
        break
    x += 1

end = datetime.now()
print( "runtime = %s" % (end - start) )