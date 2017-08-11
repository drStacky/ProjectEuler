# Recursive method for creating all permutations of integers 1 through p.
# At the bottom I use this function for problem 32 in Project Euler - Pandigital products
def get_perms(stop):
    p = []
    if stop<=1:
        p.append('1')
    else:
        # For every permutation of stop-1, insert stop in between each digit to produce new permutations
        for y_string in get_perms(stop-1):
            for j in range(len(y_string)+1):
                p.append(y_string[:j] + str(stop) + y_string[j:])
    # Results is returned as a list of strings
    return p


from datetime import datetime
start = datetime.now()

perms = get_perms(9)
# for p in permutations:
#     print( p )

pandigital_products = []

# Check for products of the form X*XXXX=XXXX
for perm in perms:
    multiplicand = int(perm[:1])
    multiplier = int(perm[1:5])
    product = int(perm[5:])
    if multiplicand * multiplier == product:
        # print( '%j * %j = %j' % (multiplicand, multiplier, product) )
        pandigital_products.append(product)

# Check for products of the form XX*XXX=XXXX
for perm in perms:
    multiplicand = int(perm[:2])
    multiplier = int(perm[2:5])
    product = int(perm[5:])
    if multiplicand * multiplier == product:
        # print( '%j * %j = %j' % (multiplicand, multiplier, product) )
        pandigital_products.append(product)

# Since 100*100 = 10000 (worst case scenario), there are no products XXX*XXX=XXX

# Sets don't allow repeats, so changing list to set and back removes possible repetitions.
pandigital_products = list( set( pandigital_products ) )
# print( pandigital_products )
total = sum(pandigital_products)
print('Total of pandigital products is', total )

# Print runtime (seconds)
end = datetime.now()
print( "runtime = %s" % (end - start) )