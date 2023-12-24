from Deck import Card


def scorer(cards: list[Card]):
    score = 0
    for card in cards:
        score += card.value
        # A can be counted as 11 or 1 depending on the player's intent. If total score <=10 A can be counted as 11
        # since 1 is the default value for A, upping range to <=11, and adding additional score of 10 points
        if card.number == 'A' and score <= 11:
            score += 10

    return score


def winnerPayoff(player, dealer, stake):
    if player.score <= 21:
        if player.score > dealer.score or dealer.score > 21:
            winner = player
        elif player.score < dealer.score:
            winner = dealer
        else:
            winner = None
    elif player.score > 21 >= dealer.score:
        winner = dealer
    else:
        winner = None

    payoff = {player: [stake, -stake], dealer: [-stake, stake], None: [0, 0]}[winner]

    return winner, payoff


def gameEnd(player, dealer):
    if player.bank > dealer.bank or dealer.bank <= 0:
        winner = player
    elif dealer.bank > player.bank or player.bank <= 0:
        winner = dealer
    else:
        winner = None

    return winner

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


def roundAuto(dealer, player, deck):
    print("\n<<<<<<<<<<<<<< ROUND START >>>>>>>>>>>>>>>>>\n")

    stake = 0
    # TODO add int checker here for input cleanup
    stake = 10
    while stake > player.bank:
        stake=player.bank

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
    return winner
