from BlackjackHelper import winnerPayoff, gameEnd
from Deck import Deck
from Player import Player, Dealer
from BlackjackHelper import *


deck = Deck()
nomduguerre = input("What is your name O Great Player?\n")
player = Player(nomduguerre)
dealer = Dealer()
bank = -1000
while bank <= 0:
    try:
        bank = int(input("Hello " + str(player.name) + " , how large do you want the bank to be?\n"))
        if bank <= 0:
            print("Yakian na karo")
    except:
        bank = -1000
        print("Yakian na karo")

player.bank = bank
dealer.bank = bank
wantToContinue = True

while wantToContinue and player.bank > 0 and dealer.bank > 0:
    round(dealer, player, deck)
    if dealer.bank <= 0 or player.bank <= 0:
        wantToContinue = False
    if wantToContinue == True:
        continueDecision = input("\n Do you want to play another Round? <Yes> <No> \n")
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
