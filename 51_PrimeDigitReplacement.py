'''
Created on Dec 27, 2016

By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated 
numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the 
smallest prime with this property.
Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

@author: mstackpo
'''
import math
from datetime import datetime

import numpy as np


def number_to_array(n: int) -> np.array:
    '''Convert number into array of digits, with idx=0 as ones place'''
    return np.array([
        n % 10**(i+1) // 10**i
        for i in range(int(math.log10(n)) + 1)
    ])


def array_to_number(digits: np.array) -> int:
    '''Converts a list of digits into a number, assuming ones place in idx=0'''
    return sum(d*10**i for i, d in enumerate(digits))


def is_prime_list(limit):
    is_prime = [True] * limit                          # Initialize the primality list
    is_prime[0] = is_prime[1] = False

    for i in range(2, limit):
        if is_prime[i]:
            for n in range(2*i, limit, i):     # Mark factors non-prime
                is_prime[n] = False

    return is_prime


def explore_prime_families(max_limit):
    is_prime = is_prime_list(2 * max_limit)
    for i in range(max_limit//2):
        if is_prime[i]:
            digits = number_to_array(i)

            for num_repeats in range(1, 4):
                d = -1
                while d < 11 - num_repeats:
                    d += 1
                    if (digits == d).sum() == num_repeats:
                        break
                if d < 11 - num_repeats:
                    locs = np.where(digits == d)[0]
                    primes = []
                    for new_d in range(d, 10):
                        if i == 1021:
                            temp = 0
                        new_digits = digits.copy()
                        new_digits[locs] = new_d
                        new_number = array_to_number(new_digits)
                        if is_prime[new_number]:
                            primes.append(new_number)
                    if len(primes) == size_prime_family:
                        return primes


if __name__ == '__main__':
    start = datetime.now()

    size_prime_family = 8

    max_limit = 1_000_000
    # max_limit = 50_000

    primes = explore_prime_families(max_limit)
    print(primes)

    end = datetime.now()
    print(f'\nruntime = {end - start}')
