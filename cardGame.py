import random

SUITE = 'H D S C'.split()# Create the suits list
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()# Create the ranks list

DECKS = [(s,r) for s in SUITE for r in RANKS]# Create the decks

random.shuffle(DECKS)# Shuffle the decks

player = DECKS[:27]# split deck evenly
computer = DECKS[27:]# split deck evenly

player_RC = random.randint(0,len(player))#create random number for player index card
computer_RC = random.randint(0,len(computer))#create random number for computer index card



while len(player) !=0 or len(computer) !=0:# Exit while loop if player or computer have no more cards
    player_RC = random.randint(0,len(player))#create random number for player index card
    computer_RC = random.randint(0,len(computer))#create random number for computer index card
    if player[player_RC] > computer[computer_RC]:#if loop if player has
        print("PLAYER WIN")
        print("The players card count is: ", len(player))
        print("The computers card count is: ", len(computer))
        computer.remove(computer[computer_RC])# Remove card from computer
        player.append(computer[computer_RC])# Add card to player

    else:
        print("PLAYER LOSE")
        print("The players card count is: ", len(player))
        print("The computers card count is: ", len(computer))
        player.remove(player[player_RC])# Remove card from computer
        computer.append(player[player_RC])# Add card to player
