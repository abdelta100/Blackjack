from Deck import Deck
from Player import Computer, Dealer
from BlackjackHelper import *

def roundMain(player, dealer):
    deck = Deck()
    #player = Computer()
    #dealer = Dealer()
    player = player
    dealer = dealer
    bank = 100
    player.bank = bank
    dealer.bank = bank
    player_wins = 0
    dealer_wins = 0
    num_rounds = 0
    wantToContinue = True

    while wantToContinue and player.bank > 0 and dealer.bank > 0:
        winner = roundAuto(dealer, player, deck)
        if dealer.bank <= 0 or player.bank <= 0:
            wantToContinue = False
        if wantToContinue:
            continueDecision = "Yes"
            if continueDecision == "No" or continueDecision == "no":
                wantToContinue = False

        player.clearHand()
        dealer.clearHand()
        player.roundPlay = True
        num_rounds += 1
        if winner == player:
            player_wins += 1
        elif winner == dealer:
            dealer_wins += 1

    winner = gameEnd(player, dealer)
    rollCredits(player, dealer, winner)

    print("Number of rounds won by player: " + str(player_wins))
    print("Number of rounds won by dealer: " + str(dealer_wins))
    print("Number of rounds drawn: " + str(num_rounds - (player_wins + dealer_wins)))
    print("Number of rounds played total: " + str(num_rounds))

    print("Thanks for playing " + player.name + " !")
    print("Bank Amount: " + str(player.bank))
    print("\n")
    print("_______________ Avengers: Endgame________________")
    return winner

player = Computer()
dealer = Dealer()
winner = roundMain(player, dealer)