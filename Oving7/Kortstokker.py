from sys import stdin
from itertools import repeat

def merge(decks):
    li = set()
    for k in decks:
    	for h in k:
    		li.add(h)
    word = ""
    for j in range(1, len(li)+1):
    	for i in li:
    		if i[0] == j:
    			word = word + i[1]
    			continue;
    return word

decks = []
for line in stdin:
    (index, list) = line.split(':')
    deck = zip(map(int, list.split(',')), repeat(index))
    decks.append(deck)
print merge(decks)