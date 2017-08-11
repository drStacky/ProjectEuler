'''
Created on Dec 29, 2016

Ex: 8C TS KC 9H 4S 7D 2S 5D 3S AC

The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards 
(separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume 
that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in 
each hand there is a clear winner.

How many hands does Player 1 win?

@author: mstackpo
'''

from datetime import datetime
start = datetime.now()

from itertools import groupby
# from collections import Counter
from collections import defaultdict


def read_cards():
    count = 0
    with open('poker.txt') as my_input:
        for line in iter(my_input):
            hands = line.split()
            count += pick_winner(hands)
    
    return count
            
def pick_winner(hands):                         # Given list of 10 (two hands), returns 1 if first player wins, 0 otherwise
    hand1 = hands[0:5]
    hand1_type = hand_type(hand1)
    hand2 = hands[5:10]
    hand2_type = hand_type(hand2)
    
    if hand1_type > hand2_type: return 1
    elif hand1_type < hand2_type: return 0
    else: return tie_breaker(hand1,hand2)

'''
    1: High Card: Highest value card.
    2: One Pair: Two cards of the same value.
    3: Two Pairs: Two different pairs.
    4: Three of a Kind: Three cards of the same value.
    5: Straight: All cards are consecutive values.
    6: Flush: All cards of the same suit.
    7: Full House: Three of a kind and a pair.
    8: Four of a Kind: Four cards of the same value.
    9: Straight Flush: All cards are consecutive values of same suit.
    (special case of 9) Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
    0: error
'''

def hand_type(hand = []):                   # Returns numeric value of hand type (see above)
    values = []
    suits = []
    for card in hand:                       # Luckily poser.txt has no 10, so first character is always value, second is suit
        values.append(card[0])
        suits.append(card[1])
    values = sorted(values)
    # groupby makes subiterator of like-valued list elements
    frequency = [len(list(group)) for key, group in groupby(values)]    # Returns frequency list of card values
    
    if len(set(suits)) == 1:
        if is_straight(values): return 9    # Straight flush
        else: return 6                      # Flush
    elif is_straight(values): return 5      # Straight (not flush)
    elif len(frequency) == 5: return 1      # High card
    elif len(frequency) == 4: return 2      # One pair
    elif len(frequency) == 3:
        if 3 in frequency: return 4         # Three of a kind
        else: return 3                      # Two pairs
    elif len(set(values)) == 2:
        if 4 in frequency: return 8         # Four of a kind
        else: return 7                      # Full house
    else: return 0

def is_straight(values):                    # Returns boolean if values are sequential
    num_values = []
    for x in values:                        # Convert face cards to numbers for easy comparison
        if x.isdigit(): num_values.append(int(x))   # Really should be refactored to use card_to_value
        else:
            if x == 'J': num_values.append(11)
            elif x == 'Q': num_values.append(12)
            elif x == 'K': num_values.append(13)
            elif x == 'A':
                num_values.append(1)
                num_values.append(14)
    
    num_values = sorted(num_values)         # Make sure cards are in order
    
    is_straight = True
    
    if len(num_values) < 5: return False    # Make sure cards are all unique
    for i in range(0,4):
        if num_values[i] + 1 != num_values[i + 1]: is_straight = False
    
    if is_straight: return True             # If ace low straight or straight up to king, return true, otherwise check for ace-high straight
    elif len(num_values) == 6:
        is_straight = True                  # Reset to check for ace-high straight
        for i in range(1,5):
            if num_values[i] + 1 != num_values[i + 1]: is_straight = False
    return is_straight

def card_to_number(hand):                   # Converts cards to numeric values, assumes aces high
    num_values = []
    for y in hand:                          # Convert face cards to numbers for easy comparison
        x = y[0]                            # Only need card values for this
        if x.isdigit(): num_values.append(int(x))
        else:
            if x == 'J': num_values.append(11)
            elif x == 'Q': num_values.append(12)
            elif x == 'K': num_values.append(13)
            elif x == 'A': num_values.append(14)
    return num_values

def tie_breaker(hand1, hand2):
    type_hand = hand_type(hand1)             # Numeric value representing type of hand (flush, striaght, etc)

    num_values1 = card_to_number(hand1)
    num_values2 = card_to_number(hand2)
    
    freq1 = defaultdict(int)
    for value in num_values1:
        freq1[value] += 1

    freq2 = defaultdict(int)
    for value in num_values2:
        freq2[value] += 1
    
    #!!! Luckily this worked, but it doesn't take into account two flushes where both hands have the same high card !!!
    high_card1 = max(num_values1)           # High Card, straight, flush, or straight flush
    high_card2 = max(num_values2)
    if type_hand == 2:                      # One Pair
        for card,freq in freq1.items():     # First check to see who has higher pair
            if freq == 2: high_card1 = card
        for card,freq in freq2.items():
            if freq == 2: high_card2 = card        
        if high_card1 == high_card2:        # If they have the same pair, look for high card of what's left
            high_card1 = max(card for card,freq in freq1.items() if freq == 1)
            high_card2 = max(card for card,freq in freq2.items() if freq == 1)
    elif type_hand == 3:                    # Two Pairs
        high_card1 = max(card for card,freq in freq1.items() if freq == 2)  # First check for highest pair
        high_card2 = max(card for card,freq in freq2.items() if freq == 2)
        if high_card1 == high_card2:        # If highest pair match, check lowest pair
            high_card1 = min(card for card,freq in freq1.items() if freq == 2)
            high_card2 = min(card for card,freq in freq2.items() if freq == 2)
        if high_card1 == high_card2:        # If both pairs match, check remaining card
            high_card1 = max(card for card,freq in freq1.items() if freq == 1)
            high_card2 = max(card for card,freq in freq2.items() if freq == 1)
    elif type_hand == 4 or type_hand == 7:  # Three of a Kind or Full House
        for card,freq in freq1.items():     # Only need to check who has highest 3 of kind (can't possibly match)
            if freq == 3: high_card1 = card
        for card,freq in freq2.items():
            if freq == 3: high_card2 = card
    elif type_hand == 8:                    # Four of a Kind
        for card,freq in freq1.items():     # Only need to check who has highest 4 of kind (can't possibly match)
            if freq == 4: high_card1 = card
        for card,freq in freq2.items():
            if freq == 4: high_card2 = card

    if high_card1 > high_card2:
        return 1
    else: return 0

###############################^^^ Function Definitions ^^^#####################################

print('Player 1 wins %i times' % read_cards())

#print(tie_breaker(['8S', 'JD', '8D', 'JD', '8H'], ['JC', 'JC', '7C', 'JD', '7C']))

end = datetime.now()
print( "runtime = %s" % (end - start) )