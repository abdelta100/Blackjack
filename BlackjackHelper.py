def scorer(cards):
    numeros = [card.split(" ")[0] for card in cards]
    score = 0
    for number in numeros:
        if number in ["J", "Q", "K"]:
            score += 10
        elif number == "A":
            score += 1
        else:
            score += int(number)

        if "A" in numeros and score <= 11:
            score += 10

    return score


def winnerPayoff(player, dealer, stake):
    if player.score > dealer.score and player.score <= 21:
        winner = player
        payoff = [stake, -stake]
    elif dealer.score > player.score and dealer.score <= 21:
        winner = dealer
        payoff = [-stake, stake]
    elif dealer.score <= 21 and player.score > 21:
        winner = dealer
        payoff = [-stake, stake]
    elif player.score <= 21 and dealer.score > 21:
        winner = player
        payoff = [stake, -stake]
    else:
        winner = None
        payoff = [0, 0]

    return winner, payoff


def gameEnd(player, dealer):
    if player.bank > dealer.bank or dealer.bank <= 0:
        winner = player
    elif dealer.bank > player.bank or player.bank <= 0:
        winner = dealer
    else:
        winner = None

    return winner
