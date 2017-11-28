# This code simulates the first part of a game of cribbage, including defining the deck,
# dealing the cards, and playing through one hand.

# Next steps are to refine the scoring methodology and allow the game to proceed until one 
# player has reached 121 points. After that, more code can be written to allow the game 
# to play itself, beginning with random play. Results can be incorporated into a machine
# learnig model to gradually improve the strategy with which to play the game, and optimize
# play


import random
from collections import Counter

deck = [{} for card in range(52)]
hand = [[{} for dealcard in range(6)] for player in range (2)]
already_dealt = [{} for card in range(52)]
cardup=0
card1 = 0
card2 = 0
thecard=0
cardpoints = 0
carduppoints = 0
crib = [{} for card in range(4)]
points = [0 for player in range(2)]


# defines the deck as a 13 x 4 matrix

for cardnum in range(13):
    deck[cardnum]["suit"] = "S"
    deck[cardnum + 13]["suit"] = "D"
    deck[cardnum + 26]["suit"] = "H"
    deck[cardnum + 39]["suit"] = "C"

    for sequence in range(4):
        deck[cardnum + (13* sequence)]["pips"] = cardnum + 1

# executes the process of a deal, in which each player recieves 6 cards, 
# randomly selected from those that remain in the deck

def deal():
    global cardup
    global carduppoints
    for player in range(2):
        for dealcard in range(6):
            still_looking = True
            while still_looking:
                    nominee = random.choice(deck)
                    if nominee not in already_dealt:
                        hand[player][dealcard] = nominee
                        already_dealt.append(nominee)
                        still_looking = False
    still_looking = True

    while still_looking:
        nominee = random.choice(deck)
        if nominee not in already_dealt:
            cardup = nominee
            carduppoints = cardup["pips"]
            already_dealt.append(nominee)
            still_looking = False

            
# allows each player to choose 2 cards from their hand for the crib

def choosecards(player):
    print "Player %s, here's your hand:" % (player + 1)
    for card in hand[player]: print hand[player].index(card),": ", card["suit"], card["pips"]
    print "The up card is %s" % cardup["suit"], cardup["pips"]
    print "\n Choose your crib cards (0-5):"

    while True:
        card1 = input("First card: ")
        if card1 > 5:
            print "Your number must be between 0 and 5"
            continue
        else:
            break

    while True:
        card2 = input("Second card: ")
        if card2> 5 or card1==card2:
            print "Your number must be valid."
            continue
        else:
            break

    print "\nYou selected %s %s and %s %s." % (hand[player][card1]["suit"],hand[player][card1]["pips"], hand[player][card2]["suit"],hand[player][card2]["pips"])

    crib[player * 2] = hand[player][card1]
    crib[(player * 2) + 1] = hand[player][card2]
    hand[player][card1] = None
    hand[player][card2] = None
    

# proceeds through the play of individual cards within a hand.

def play():
    for player in range(2): points[player] = 0
    thecount = 0

    cardsplayed = 0
    player = 1

    while cardsplayed <8:

        print "\n\nPlayer %s, here's your hand:" % (player + 1)
        for card in hand[player]:
                if card != None:
                    print hand[player].index(card),": ", card["suit"], card["pips"]

        while True:
            thecard = input("Player X, play a card: ")
            if thecard == 9:
                print "Go!!!"
                thecount = 0
                player = 1-player
                break
            elif thecount + hand[player][thecard]["pips"] >31:
                print "You may not exceed 31. Play another card or type 9 for Go"
                continue
            else:
                break

            recent[cardsplayed] = hand[player][thecard]

        if card1 <> 9:
            cardpoints = hand[player][thecard]["pips"]
            thecount = thecount + cardpoints
            hand[player][thecard] = None
            cardsplayed += 1
            player = 1-player
            print "\nThe count is ", thecount

        print "\nTotal cards played: ", cardsplayed

        counthand(player, cardpoints, )

def counthand(player, cardpoints):
    if carduppoints: print "The card up is ", carduppoints


deal()
for player in range(2): choosecards(player)
play()

print "Player 1 has", points[0]
print "Player 2 has", points[1]
