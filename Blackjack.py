from BlackjackHelper import winnerPayoff, gameEnd
from Deck import Deck
from Player import Player, Dealer


def rollCredits(player, dealer, winner):
    if winner == None:
        print("The game is drawn")
        print("Player Bank: " + str(player.bank))
        print("Dealer Bank: " + str(dealer.bank))
    else:
        print("The winner of the game is " + winner.name)
        print("Player Bank: " + str(player.bank))
        print("Dealer Bank: " + str(dealer.bank) + "\n")

    print("Please visit Casino Python again! \nAlways a Pleasure to take your Money!\n")


def currentState(dealer, player, deck):
    print("__________________________ \n Your Cards")
    for card in player.hand: print(card)

    print("__________________________ \n Dealer's Card")
    print(dealer.hand[0])


def endState(dealer, player, deck):
    print("__________________________ \n Your Cards")
    for card in player.hand: print(card)

    print("__________________________ \n Dealer's Card")
    for card in dealer.hand: print(card)


def round(dealer, player, deck):
    print("\n<<<<<<<<<<<<<< ROUND START >>>>>>>>>>>>>>>>>\n")

    stake = 0
    # TODO add int checker here for input cleanup
    stake = int(input("How much would you like to bet?\n"))
    while stake > player.bank:
        try:
            stake = int(input("Jani dobara try mar\n"))
        except:
            stake = player.bank * 2

    player.drawCard(deck)
    dealer.drawCard(deck)
    player.drawCard(deck)

    while player.score < 21:
        currentState(dealer, player, deck)
        player.turn(deck)
        if not player.roundPlay:
            print('\nYou have chosen to not Draw Any Cards, the round has ended\n')
            break

    while dealer.score < 17:
        dealer.drawCard(deck)

    print("player Score: " + str(player.score))
    print("dealer Score: " + str(dealer.score))

    endState(dealer, player, deck)

    winner, payoff = winnerPayoff(player, dealer, stake)
    player.bank += payoff[0]
    dealer.bank += payoff[1]

    if winner == None:
        print("\nThe round is drawn")
        print("Player Bank: " + str(player.bank))
        print("Dealer Bank: " + str(dealer.bank))
    else:
        print("\nThe winner is " + winner.name)
        print("Player Bank: " + str(player.bank))
        print("Dealer Bank: " + str(dealer.bank))

    print("\n<<<<<<<<<<<<<< ROUND END >>>>>>>>>>>>>>>>>\n")


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
