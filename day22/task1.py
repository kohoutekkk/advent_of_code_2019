from collections import deque

decks_file = open('data/test_in.txt')
#decks_file = open('data/in.txt')

deck1, deck2 = decks_file.read().split('\n\n')


class Deck():
    def __init__(self, deck_list):
        self._deck = deque(deck_list)

    def empty(self):
        return not self._deck

    def push(self, card):
        self._deck.append(card)

    def pop(self):
        return self._deck.popleft()

    def score(self):
        s = 0

        for i,c in enumerate(reversed(self._deck)):
            s += (i+1)*c

        print(s)



    def __repr__(self):
        return repr(self._deck)

    def __str__(self):
        return str(self._deck)

    def __len__(self):
        return len(self._deck)

deck1 = Deck([int(card) for card in deck1.split('\n')[1:]])
deck2 = Deck([int(card) for card in deck2.split('\n')[1:]])


def play_round(d1, d2):
    c1 = d1.pop()
    c2 = d2.pop()


    if c1 > c2:
        d1.push(c1)
        d1.push(c2)


    if c2 > c1:
        d2.push(c2)
        d2.push(c1)

    return d1, d2



while not deck1.empty() and not deck2.empty():
    deck1, deck2 = play_round(deck1, deck2)


if not deck1.empty():
    deck1.score()

if not deck2.empty():
    deck2.score()