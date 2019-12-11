"""
Python Blackjack Game
Improvements:
    Increase number of players
    
"""
import random

class person:
    def __init__(self, name, chips, bet, hand, c_val, st, sur, index):
        self.name = name
        self.chips = chips
        self.bet = bet
        self.hand = hand
        self.c_val = c_val
        self.st = st
        self.sur = sur
        self.index = index
        
deck_s = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
deck_v = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

player = person("Player", 1000, [], [], [], [0,0,0,0], 0, 0)
dealer = person("Dealer", 1000, [], [], [], 0, 0, 0)

def cardsetup():
    a, b = int(random.random() * 13), int(random.random() * 13)
    c, d = int(random.random() * 13), int(random.random() * 13)
    player.hand.append([deck_s[a], deck_s[b]])
    player.c_val.append([deck_v[a], deck_v[b]])
    dealer.hand = [deck_s[c], deck_s[d]]
    dealer.c_val = [deck_v[c], deck_v[d]]
    
def setbet():
    print("{} Chips: {}".format(player.name, player.chips))
    print("{} Chips: {}".format(dealer.name, dealer.chips))
    bet = int(input("Input Your Bet: "))
    player.bet.append(bet)
    player.chips -= bet
    dealer.bet.append(bet)
    dealer.chips -= bet

def nameset():
    print("Input Player Name")
    namep = input("Input Name: ")
    player.name = namep
    
def action():
    command = input("Player Turn, Command Choices: \n -Hit \n -Double \n -Insurance \n -Split \n -Stand \n -Surrender \n -Quit \nInput Command: ").lower()
    if command == "hit":
        hit()
        score()
        wincond()
    elif command == "double":
        doubledown()
        score()
        wincond()
    elif command == "insurance":
        insurance()
        score()
        wincond()
    elif command == "split":
        split()
        score()
        wincond()
    elif command == "stand":
        stand()
        score()
        wincond()
    elif command == "surrender":
        player.sur = 1
        print("Player Surrenders")
        score()
        wincond()
    elif command == "quit":
        print("Program Terminated")
    else:
        print("Wrong Command, Try Again")
        action()
        
def acecheck():
    for i in player.c_val:
        if sum(i) > 21 and (11 in player.c_val) == True:
            i.remove(11)
            i.append(1)
    if sum(dealer.c_val) > 21 and (11 in player.c_val) == True:
            dealer.c_val.remove(11)
            dealer.c_val.append(1)

def hit():
    i = player.index
    r = int(random.random() * 13)
    player.hand[i].append(deck_s[r])
    player.c_val[i].append(deck_v[r])
    acecheck()
    print("Player Hits")
    if sum(player.c_val[i]) >= 21:
        player.index += 1
        print("Cannot Hit, Next")
        player.st[i] = 1 
        if sum(player.c_val[i]) > 21: 
            print("Player Busts")

            
def doubledown():
    i = player.index
    if len(player.c_val[i]) <= 2:
        player.chips -= player.bet[i]
        player.bet[i] = (player.bet[i] * 2)
        dealer.chips -= dealer.bet[i]
        dealer.bet[i] = (dealer.bet[i] * 2)
        print("Player Doubles Down")
        hit()
        if sum(player.c_val[i]) < 21:
            stand()
    else:
        print("Cannot Double")
        
def insurance():
    if dealer.hand[0] == "A":
        dealer.sur = (dealer.bet[0] * 0.5)
        player.chips -= (dealer.bet[0] * 0.5)
        print("Player Insures")
    else:
        print("Cannot Insure")
        
def split():
    if player.index <= 3:
        i = player.index
        player.hand.append([player.hand[i][1]])
        player.hand[i].remove(player.hand[i][1])
        player.c_val.append([player.c_val[i][1]])
        player.c_val[i].remove(player.c_val[i][1])
        player.bet.append(player.bet[0])
        player.chips -= player.bet[0]
        dealer.bet.append(dealer.bet[0])
        dealer.chips -= dealer.bet[0]
        print("Player Splits")
    else:
        print("Cannot Split")

def stand():
    if player.index > 3:
        wincond()
    else:
        player.st[player.index] = 1
        player.index += 1
        print("Player Stands")
    
def score():
    acecheck()
    dealerhid = [dealer.hand[0], "X"]    
    print("--------Score--------")
    print(player.name)
    for i in range(len(player.c_val)):
        print("Score: " + str(sum(player.c_val[i])))
        print(player.hand[i])
        print("Bet: " + str(player.bet[i]))
    print("---------------------")
    print(dealer.name)
    print("Score: X")
    print(dealerhid)
    print("Bet: " + str(sum(dealer.bet)))
    print("---------------------")
    
def wincond():
    if player.sur == 1:
        dealer.chips += (dealer.bet[0] * 2)
        print("{} Wins {} Chips!".format(dealer.name, dealer.bet[0]))
        restart()
    elif sum(dealer.c_val) == 21:
        dealer.chips += (dealer.bet[0] * 2)
        print("Dealer Blackjack!")
        print("{} Wins {} Chips!".format(dealer.name, dealer.bet[0]))
        if dealer.sur != 0:
            player.chips += (dealer.sur * 2)
            print("Insurance, {} Wins {} Chips!".format(player.name, (dealer.sur*2)))
        restart()
    elif sum(player.c_val[0]) == 21 and len(player.c_val) == 1:
        player.chips += (player.bet[0] * 2)
        print("{} Blackjack!".format(player.name))
        print("{} Wins {} Chips!".format(player.name, player.bet[0]))
        restart()
    elif sum(player.st) >= len(player.c_val):
        dealerai()
        win = []        
        for i in player.c_val:
            d = sum(dealer.c_val)
            if sum(i) > d and sum(i) <= 21:
                win.append(1)
            elif d > 21:
                win.append(1)
            elif sum(i) < d and sum(i) < 21:
                win.append(-1)
            elif sum(i) > 21:
                win.append(-1)
            elif sum(i) == d and sum(i) < 21:
                win.append(0)
        
        acecheck()
        print("--------Score--------")
        print(player.name)
        for i in range(len(player.c_val)):
            print("Score: " + str(sum(player.c_val[i])))
            print(player.hand[i])
            print("Bet: " + str(player.bet[i]))
        print("---------------------")
        print(dealer.name)
        print("Score: " + str(sum(dealer.c_val)))
        print(dealer.hand)
        print("Bet: " + str(sum(dealer.bet)))
        print("---------------------")
        
        for i in range(len(win)):
            if win[i] == 1:
                player.chips += (player.bet[i] * 2)
                print("{} Wins {} Chips!".format(player.name, player.bet[i]))
            elif win[i] == -1:
                dealer.chips += (dealer.bet[i] * 2)
                print("{} Wins {} Chips!".format(dealer.name, dealer.bet[i]))
            elif win[i] == 0:
                dealer.chips += dealer.bet[i]
                player.chips += player.bet[i]
                print("Player Draws")
        restart()
        
    else:
        action()

def dealerhit():
    r = int(random.random() * 13)
    dealer.hand.append(deck_s[r])
    dealer.c_val.append(deck_v[r])
    acecheck()
    print("Dealer Hits")
    if sum(dealer.c_val) > 21: 
        print("Dealer Busts")
        dealer.st = 1 
    dealerai()
    
def dealerai():
    r = int(random.random() * 13)
    if sum(dealer.c_val) <= 11:
        dealerhit()
    elif sum(dealer.c_val) < 14 and r > 7:
        dealerhit()
    else:
        dealer.st = 1
        print("Dealer Stands")

def restart():
    command = input("Want to Play Again? \n[y/n]: ")
    if command == "y":
        player.bet = []
        player.hand = []
        player.c_val = []
        player.st = [0,0,0,0]
        player.sur = 0
        player.index = 0
        dealer.bet = []
        dealer.hand = []
        dealer.c_val = []
        dealer.st = 0
        dealer.sur = 0
        dealer.index = 0
        setbet()
        cardsetup()
        score()
        wincond()
    elif command == "n":
        print("Program Terminated")
    else:
        print("Wrong Command, Try Again")
        restart()

def gamestart():
    print("Welcome to My Blackjack Game!")
    command = input("Press Enter to Start")
    if command == "":
        nameset()
        setbet()
        cardsetup()
        score()
        wincond()
    else:
        gamestart()
        
gamestart()
    
    
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    