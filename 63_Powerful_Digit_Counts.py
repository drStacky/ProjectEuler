'''
Created on Dec 6, 2023

The 5-digit number, 16807 = 7^5, is also a fifth power. Similarly, the 9-digit number,
134217728 = 8^9, is a ninth power.

How many n-digit positive integers exist which are also an n-th power?
'''
from datetime import datetime


if __name__ == '__main__':
    start = datetime.now()

    '''NOTE:if b >= 10, b^n >= 10^n, which has n+1 digits.
    So an upper bound comes from solving 9^n > 10^(n-1) for n.
    n < 1 / (1 - log10(9)) ~ 22
    '''

    count = 0
    for b in range(1, 10):
        for n in range(0, 22):
            power = b**n
            x = len(str(power))
            if b == 9 and n == 1:
                tmp = 0
            if x == n:
                count += 1
    print(count)

    end = datetime.now()
    print(f'\nruntime = {end - start}')
