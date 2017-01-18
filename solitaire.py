from __future__ import division
import random

desired_games = 1000

# Build a deck of cards 
# Note: I'm sure there is a sexy list comprehension out there for this
suits = ['h', 'd', 'c', 's']
faces = ['J', 'Q', 'K', 'A']

cards = []
for suit in suits:
    for number in range(2, 11):
        cards.append((number, suit))
    for face in faces:
        cards.append((face, suit))


# Recursive function to check open faced cards for any matches
def checkcards(flipped_cards):
    if len(flipped_cards) > 3:
        # no sense checking cards if less than three
        if flipped_cards[-1][0] == flipped_cards[-4][0]:
            # remove last 4 cards
            del flipped_cards[-4:]
        elif flipped_cards[-1][1] == flipped_cards[-4][1]:
            # remove 2 middle cards between matching suits
            del flipped_cards[-3:-1]
            # recheck to see if any numbers line up
            checkcards(flipped_cards)

wins = 0
losses = 0

# Loop through desired amount games
for a in range(0, desired_games):
    flipped_cards = []
    # shuffle teh deck
    seed = random.random()
    random.seed(seed)
    random.shuffle(cards)
    for card in cards:
        # loop through cards "flipping them over"
        flipped_cards.append(card)
        checkcards(flipped_cards)
    if len(flipped_cards):
        losses += 1
        winlose = "Lose - {0} cards remaining".format(len(flipped_cards))
    else:
        wins += 1
        winlose = "Win!"
        # print("Game #{0}: {1} - {2}".format(a, seed, winlose))
        
print("Winning percentage: {0}% ({1} wins out of {2} shuffles)".format((wins/desired_games)*100, wins, desired_games))
