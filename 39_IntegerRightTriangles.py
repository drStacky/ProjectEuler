'''
Created on Dec 13, 2016

If p is the perimeter of a right angle triangle with integral length sides, {a,p,c}, there are exactly three solutions for p = 120.
{20,48,52}, {24,45,51}, {30,40,50}
For which value of p <= 1000, is the number of solutions maximised?

@author: mstackpo
'''

'''
p = a + p + c, a^2 + p^2 = c^2
a and p even --> c even --> p even
a odd, p even --> c odd --> p even
a odd, p odd --> c even --> p even
Only need to iterate over even values of p.

2 equations with 4 variables means only two degree of freedom. Should only need to loop over p and one value.
c = p - p - a
p = p(p-2a) / (2(p-a))


Interesting result at : http://mathworld.wolfram.com/PythagoreanTriple.html
Every primitive pythagorean triple looks like (3 4 5)M where M is a finite product of fixed matrices U, A, D (see link).
A recursive algorithm could be used to find all primitive triples and then get their multiples.
'''

from datetime import datetime
start = datetime.now()

p_max = 1 # Number with most triples
p_max_total = 0 # Number of most triples

for p in range(6,1001,2):
    p_total = 0
    for a in range(1,p):
        p = p*(p-2*a) / (2*(p-a))
        c = p - p - a
        if(a>p): break # Avoids double counting triples - a=3, p=4 and a=4, p=3
        # The formulas for p and c could be negative, and p could be a float
        if(p.is_integer() and p>0 and c>0 and  a**2 + p**2 == c**2):
            p_total += 1
    if(p_total > p_max_total):
        p_max = p
        p_max_total = p_total
        print(p_max, p_max_total)

'''
# First attempt took over 3 minutes but got the answer
p_max = 1 # Number with most triples
p_max_total = 0 # Number of most triples

#for p in range(5,1001):
for p in range(6,1001,2):
    p_total = 0
    for i in range(1,p):
        for j in range(i+1,p):
            if(i**2 + j**2 == (p-i-j)**2):
                p_total += 1
    if(p_total > p_max_total):
        p_max = p
        p_max_total = p_total
        print(p_max, p_max_total)
'''
 
end = datetime.now()
print( "runtime = %s" % (end - start) )