from Deck import Deck
from Player import Computer, Dealer
from BlackjackHelper import *

deck = Deck()
player = Computer()
dealer = Dealer()
bank = 1000

player.bank = bank
dealer.bank = bank
wantToContinue = True

while wantToContinue and player.bank > 0 and dealer.bank > 0:
    roundAuto(dealer, player, deck)
    if dealer.bank <= 0 or player.bank <= 0:
        wantToContinue = False
    if wantToContinue:
        continueDecision = "Yes"
        if continueDecision == "No" or continueDecision == "no":
            wantToContinue = False

    player.clearHand()
    dealer.clearHand()
    player.roundPlay = True

winner = gameEnd(player, dealer)
rollCredits(player, dealer, winner)

print("Thanks for playing " + player.name + " !")
print("Bank Amount: " + str(player.bank))
print("\n")
print("_______________ Avengers: Endgame________________")
