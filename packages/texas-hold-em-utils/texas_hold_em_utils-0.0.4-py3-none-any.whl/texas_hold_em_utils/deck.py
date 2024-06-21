from texas_hold_em_utils.card import Card

import random


class Deck:
    def __init__(self):
        self.cards = []
        for suit in [0, 1, 2, 3]:
            for value in range(0, 13):
                self.cards.append(Card().from_ints(value, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

    def remove(self, card):
        self.cards.remove(card)

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        return str([str(card) for card in self.cards])
