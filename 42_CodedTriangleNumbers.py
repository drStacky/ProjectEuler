'''
Created on Dec 15, 2016

The nth term of the sequence of triangle numbers is given by, tn = n(n+1)/2; so the first ten triangle numbers are:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value.
For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.
Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words,
how many are triangle words?

@author: mstackpo
'''

from datetime import datetime
start = datetime.now()

import re, string

my_input = open('words.txt')    # Create file object
text = my_input.read()          # Read in text of file object
words = re.split('"|,' ,text)   # Splits text, but leaves empty strings where successive cuts are made
words = filter(None, words)     # Removes empty strings from the list, returns an iterator

letter2number = {}
for letter, number in zip(string.ascii_uppercase, range(1, 27)):      # Creates dictionary of letter/number pairs
    letter2number[letter] = number

triangle_numbers = []                       # Create a list to hold triangle numbers
for n in range(1,100):
    triangle_numbers.append(n*(n+1)/2)

total = 0

for word in words:
    word_total = 0
    for letter in word:
        word_total += letter2number[letter]
    if(word_total in triangle_numbers):
        total += 1

print(total)

my_input.close()                # Don't forget to close the file when done

end = datetime.now()
print( "runtime = %s" % (end - start) )