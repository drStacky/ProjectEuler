'''
Created on Dec 5, 2023

The cube,41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3)
and 66430125 (405^3). In fact, 41063625 is the smallest cube which has exactly three permutations
of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.

(1st with 4 permutations is 1002^3 = 1_006_012_008)
'''
from datetime import datetime


if __name__ == '__main__':
    start = datetime.now()

    num_cubes = 5

    cube_dict = dict()
    n = 0
    while True:
        cube = n**3
        cube_str = tuple(sorted(str(cube)))
        cubes = cube_dict.get(cube_str, []) + [cube]
        if len(cubes) == num_cubes:
            print(min(cubes))
            break
        cube_dict[cube_str] = cubes
        n += 1

    end = datetime.now()
    print(f'\nruntime = {end - start}')
