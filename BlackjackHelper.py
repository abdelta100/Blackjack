from Deck import Card


def scorer(cards: list[Card]):
    # numeros = [card.split(" ")[0] for card in cards]
    score = 0
    for card in cards:
        score += card.value
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
