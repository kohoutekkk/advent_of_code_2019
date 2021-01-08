from collections import deque
import time

#decks_file = open('data/test_in.txt')
decks_file = open('data/in.txt')

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


def play_recursive(d1,d2):
    d1_set = set()
    d2_set = set()
    while not d1.empty() and not d2.empty():


        d1_strings = [str(i) for i in list(d1._deck)]
        d2_strings = [str(i) for i in list(d2._deck)]
        d1_str = ''.join(d1_strings)
        d2_str = ''.join(d2_strings)
        #
        # print(d1_str)
        # print(d1_set)
        # print(d2_set)
        if d1_str in d1_set and d2_str in d2_set:
            return 1

        d1_set.add(d1_str)
        d2_set.add(d2_str)

        #print(d1_set)
        #
        # print(d1)
        # print(d2)
        c1 = d1.pop()
        c2 = d2.pop()

        #print(c1 >= len(d1))
        #print(c2 >= len(d2))
        #print()
        #print(c1,' ',len(d1))
        #print(c2, ' ',len(d2))

        #print(c1, c2)
        #time.sleep(2)
        if c1 <= len(d1) and c2 <= len(d2):
            #print('subloop')
            sub_d1 = Deck(list(d1._deck)[:c1])
            sub_d2 = Deck(list(d2._deck)[:c2])

            winner = play_recursive(sub_d1, sub_d2)

            if winner == 1:
                d1.push(c1)
                d1.push(c2)
            else:
                d2.push(c2)
                d2.push(c1)

        else:
            #print('play')
            if c1 > c2:
                d1.push(c1)
                d1.push(c2)
            if c2 > c1:
                d2.push(c2)
                d2.push(c1)

    if d1.empty():
        return 2
    else:
        return 1


    #print('out')
    return winner

print(play_recursive(deck1, deck2))

deck2.score()
deck1.score()