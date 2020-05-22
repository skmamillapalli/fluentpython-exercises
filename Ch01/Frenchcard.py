#!/usr/bin/env python
import collections
import random
# card can have suit(Heart, Diamond, Spade, Club) and rank

card = collections.namedtuple('Card', ['suit', 'rank'])
class FrenchDeck:
    """Represents Deck of cards"""
    def __init__(self):
    	self._cards = [card(rank, suit)  for rank in ['Heart', 'Diamond', 'Spade', 'Club'] for suit in list(range(2,11))+list('JQKA')]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, i):
        # Slice object when slice notation is used, which is handled in int
        # 40 <class 'int'>
        # Card(suit='Club', rank=3)
        # slice(12, None, 13) <class 'slice'>
        print(i, type(i))
        # Handling of actual work to another object, Composition - > A way of delegation
        return self._cards[i]

cards = FrenchDeck()
print(len(cards))
print(cards[-1])

# Leverage sequence type, again benefit of sticking to data model
print(random.choice(cards))

# Print every 13th card, support for slicing by python framework
print(cards[12::13])

# Support for interation, need either iter or getitem
for card in cards:
    print(card)



