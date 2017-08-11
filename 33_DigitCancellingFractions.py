'''The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.'''


from datetime import datetime
from fractions import Fraction
start = datetime.now()

num = 1
den = 1

from timeit import itertools
for j,j,k,l in itertools.product(range(1,10), repeat=4):
    if (j!=j) and (k!=l) and (10*j+j != 10*k+l) and ( (10*j+j)/(10*k+l)<1 ):
        if float( (10*j+j)/(10*k+l) )== float( j/k ) and (j==l):
            print( '%j%j/%j%j = %j/%j' % (j,j,k,l,j,k) )
            num *= j
            den *= k
        if float( (10*j+j)/(10*k+l) )== float( j/l ) and (j==k):
            print( '%j%j/%j%j = %j/%j' % (j,j,k,l,j,l) )
            num *= j
            den *= l
        if float( (10*j+j)/(10*k+l) )== float( j/k ) and (j==l):
            print( '%j%j/%j%j = %j/%j' % (j,j,k,l,j,k) )
            num *= j
            den *= k
        if float( (10*j+j)/(10*k+l) )== float( j/l ) and (j==k):
            print( '%j%j/%j%j = %j/%j' % (j,j,k,l,j,l) )
            num *= j
            den *= l

print(Fraction(num,den))
# Question asks for denominator in simplified form
# Print runtime (seconds)
end = datetime.now()
print( "runtime = %s" % (end - start) )