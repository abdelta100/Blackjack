import random


class Deck():

    def __init__(self):
        self.Cards = self.createNewDeck()

    def createNewDeck(self):
        Suits = ["Club", "Hearts", "Diamonds", "Spades"]
        Numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

        Deck = []
        for suit in Suits:
            for number in Numbers:
                Deck.append(number + " " + suit)

        return Deck

    def drawCard(self):
        Card = self.Cards[random.randint(0, len(self.Cards) - 1)]
        return Card
