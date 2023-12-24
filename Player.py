import random

from BlackjackHelper import scorer


class Player():
    def __init__(self, name):
        self.hand = []
        self.score = 0
        self.name = name
        self.bank = 0
        self.roundPlay = True

    def drawCard(self, Deck):
        self.hand.append(Deck.drawCard())
        self.scorer()

    def scorer(self):
        self.score = scorer(self.hand)

    def clearHand(self):
        self.hand = []
        self.score = 0

    def turn(self, deck):
        choice = input("<Draw> Card or <Stop>\n")

        if choice == "Draw" or choice == 'draw':
            self.drawCard(deck)

        elif choice == "stop" or choice == 'Stop':
            self.roundPlay = False

        else:
            print("bhai nakhray na karo\n")
            self.turn(deck)


class Dealer(Player):
    def __init__(self, name='dealer'):
        super().__init__(name)

class Computer(Player):
    def __init__(self, name='Computer'):
        super().__init__(name)

    def turn(self, deck):
        choice=self.makeDecision()
        if choice == "Draw" or choice == 'draw':
            self.drawCard(deck)
        else:
            self.roundPlay = False

    def makeDecision(self):
        # using random decision for now
        dec = random.randint(0,1)
        choice = {0: "Stop", 1: "Draw"}[dec]
        return choice