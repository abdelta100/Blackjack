import random

def scorer(cards):
    numeros=[card.split(" ")[0]for card in cards]
    score=0
    for number in numeros:
        if number in ["J","Q","K"]:
            score+=10
        elif number=="A":
            score+=1
        else:
            score+=int(number)

        if "A" in numeros and score<=11:
            score+=10
            
    return score

def winnerPayoff(player, dealer, stake):
    if player.score>dealer.score and player.score<=21:
        winner=player
        payoff=[stake, -stake]
    elif dealer.score>player.score and dealer.score<=21:
        winner=dealer
        payoff=[-stake, stake]
    elif dealer.score<=21 and player.score>21:
        winner=dealer
        payoff=[-stake, stake]
    elif player.score<=21 and dealer.score>21:
        winner=player
        payoff=[stake, -stake]
    else:
        winner=None
        payoff=[0, 0] 
    
    return winner, payoff

def gameEnd(player,dealer):
    if player.bank>dealer.bank or dealer.bank<=0:
        winner=player
    elif dealer.bank>player.bank or player.bank<=0:
        winner=dealer
    else:
        winner=None

    return winner

def rollCredits(player,dealer,winner):
    if winner==None:
        print("The game is drawn")
        print("Player Bank: "+str(player.bank))
        print("Dealer Bank: "+str(dealer.bank))
    else:
        print("The winner of the game is "+winner.name)
        print("Player Bank: "+str(player.bank))
        print("Dealer Bank: "+str(dealer.bank)+"\n")

    print("Please visit Casino Python again! \nAlways a Pleasure to take your Money!\n")

class Deck():

    def __init__(self):
        self.Cards=self.createNewDeck()

    def createNewDeck(self):
        Suits=["Club","Hearts","Diamonds", "Spades"]
        Numbers=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

        Deck=[]
        for suit in Suits:
            for number in Numbers:
                Deck.append(number+" "+suit)

        return Deck
    
    def drawCard(self):
        Card=self.Cards[random.randint(0,len(self.Cards)-1)]
        return Card

class Dealer():
    def __init__(self):
        self.hand=[]
        self.score=0
        self.name="Dealer"
        self.bank=0
    
    def drawCard(self,Deck):
        self.hand.append(Deck.drawCard())
        self.scorer()

    def clearHand(self):
        self.hand=[]
        self.score=0
    
    def scorer(self):
        self.score=scorer(self.hand)

class Player():
    def __init__(self, name):
        self.hand=[]
        self.score=0
        self.name=name
        self.bank=0
        self.roundPlay=True
    
    def drawCard(self,Deck):
        self.hand.append(Deck.drawCard())
        self.scorer()
    
    def scorer(self):
        self.score=scorer(self.hand)

    def clearHand(self):
        self.hand=[]
        self.score=0
    
    def turn(self, deck):
        choice=input("<Draw> Card or <Stop>\n")

        if choice=="Draw" or choice== 'draw':
            self.drawCard(deck)
        
        elif choice=="stop" or choice== 'Stop':
            self.roundPlay=False

        else:
            print("bhai nakhray na karo\n")
            self.turn(deck)

def currentState(dealer, player,deck):
    print("__________________________ \n Your Cards")
    for card in player.hand: print(card)

    print("__________________________ \n Dealer's Card")
    print(dealer.hand[0])

def endState(dealer, player,deck):
    print("__________________________ \n Your Cards")
    for card in player.hand: print(card)

    print("__________________________ \n Dealer's Card")
    for card in dealer.hand: print(card)

def round(dealer, player,deck):

    print("\n<<<<<<<<<<<<<< ROUND START >>>>>>>>>>>>>>>>>\n")

    stake=0
    stake=int(input("How much would you like to bet?\n"))
    while stake>player.bank:
        try:
            stake=int(input("Jani dobara try mar\n"))
        except:
            stake=player.bank*2

    player.drawCard(deck)
    dealer.drawCard(deck)
    player.drawCard(deck)
    

    while player.score<21:
        currentState(dealer,player,deck)
        player.turn(deck)
        if not player.roundPlay:
            print('\nYou have chosen to not Draw Any Cards, the round has ended\n')
            break

    while dealer.score<17:
        dealer.drawCard(deck)

    print("player Score: "+str(player.score))
    print("dealer Score: "+str(dealer.score))

    endState(dealer,player,deck)

    winner, payoff= winnerPayoff(player,dealer,stake)
    player.bank+=payoff[0]
    dealer.bank+=payoff[1]

    if winner==None:
        print("\nThe round is drawn")
        print("Player Bank: "+str(player.bank))
        print("Dealer Bank: "+str(dealer.bank))
    else:
        print("\nThe winner is "+winner.name)
        print("Player Bank: "+str(player.bank))
        print("Dealer Bank: "+str(dealer.bank))

    print("\n<<<<<<<<<<<<<< ROUND END >>>>>>>>>>>>>>>>>\n")
    
        


deck=Deck()
nomduguerre=input("What is your name O Great Player?\n")
player=Player(nomduguerre)
dealer=Dealer()
bank=-1000
while bank<=0:
        try:
            bank=int(input("Hello "+str(player.name)+" , how large do you want the bank to be?\n"))
            if bank<=0:
                print("Yakian na karo")
        except:
            bank=-1000
            print("Yakian na karo")
        

player.bank=bank
dealer.bank=bank
wantToContinue=True

while wantToContinue and player.bank>0 and dealer.bank>0:
    round(dealer, player, deck)
    if dealer.bank<=0 or player.bank<=0:
        wantToContinue=False
    if wantToContinue==True:
        continueDecision =input("\n Do you want to play another Round? <Yes> <No> \n" )
        if continueDecision=="No" or continueDecision=="no":
            wantToContinue=False
        
    player.clearHand()
    dealer.clearHand()
    player.roundPlay=True

winner=gameEnd(player,dealer)
rollCredits(player,dealer,winner)

print("Thanks for playing "+player.name+" !")
print("Bank Amount: "+str(player.bank))
print("\n")
print("_______________ Avengers: Endgame________________")
