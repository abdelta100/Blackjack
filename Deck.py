import random


class Deck():
    #TODO multiple decks in game with replacement,
    # also maybe figure out a way to prevent all cards being consumed

    def __init__(self):
        self.Cards = self.createNewDeck()

    def createNewDeck(self):
        Suits = ["Club", "Hearts", "Diamonds", "Spades"]
        Numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

        Deck = []
        for suit in Suits:
            for number in Numbers:
                Deck.append(Card(number, suit))

        return Deck

    def drawCard(self):
        Card = self.Cards[random.randint(0, len(self.Cards) - 1)]
        return Card


class Card:
    def __init__(self, number: str, suit: str):
        self.number = number
        self.suit = suit
        self.value = self.getValue()

    def getValue(self):
        try:
            value = int(self.number)
            return value
        except:
            value = {"A": 1, "J": 10, "Q": 10, "K": 10}[self.number]
            return value

    def __repr__(self):
        rep=self.number + ' ' + self.suit
        return rep

    def __str__(self):
        rep = self.number + ' ' + self.suit
        return rep
