from Player import Computer, Dealer
from BlackJackAuto import roundMain

player = Computer()
dealer = Dealer()
player_wins = 0
dealer_wins = 0
num_games = 0
games_to_play = 100

for i in range(games_to_play):
    num_games+=1
    winner = roundMain(player, dealer)
    if winner == player:
        player_wins += 1
    elif winner == dealer:
        dealer_wins += 1
        

print("Number of whole games won by player: " + str(player_wins))
print("Number of whole games by dealer: " + str(dealer_wins))
print("Number of whole games played total: " + str(num_games))