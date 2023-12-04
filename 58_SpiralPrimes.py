'''
Created on Dec 1, 2023

Starting with
 and spiralling anticlockwise in the following way, a square spiral with side length
 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that
 out of the  numbers lying along both diagonals are prime; that is, a ratio of 8/3 ~ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be
formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along
both diagonals first falls below 10%?

@author: mstackpo
'''
from datetime import datetime

from euler import is_prime


if __name__ == '__main__':
    start = datetime.now()

    diagonal = [1]

    n = 0
    prime_count = 0
    diagonal_count = 1
    ratio = prime_count / diagonal_count
    while ratio >= 0.1 or n == 0:
        n += 1
        new_prime_candidates = [(2*n+1)**2 - i * 2 * n for i in range(1, 4)]
        # diagonal += new_diagonal_elements
        prime_count += sum(is_prime(d) for d in new_prime_candidates)
        diagonal_count += 4
        ratio = prime_count / diagonal_count

    print(f'{ratio}')
    print(f'{2 * n + 1}')

    end = datetime.now()
    print(f'\nruntime = {end - start}')
