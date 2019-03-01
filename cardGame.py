import random

SUITE = 'H D S C'.split()# Create the suits list
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()# Create the ranks list

DECKS = [(s,r) for s in SUITE for r in RANKS]# Create the decks

random.shuffle(DECKS)# Shuffle the decks

player = DECKS[:26]# split deck evenly
computer = DECKS[26:]# split deck evenly





while len(player) != 0 or len(computer) != 0:#while loop to keep on playing until one of the players card reach zero
        print("The players card count is: " , len(player))# Output of how much cards player have
        print("The computers card count is: ", len(computer))# Output of how much cards player have
        plrRandom = random.randint(0, len(player)-1)# Create a random number to use as which index to use
        cmpRandom = random.randint(0, len(computer)-1)# Create a random number to use as which index to use
        plrCard = player.pop((plrRandom))# Pop of random number and store in variable
        comCard = computer.pop((cmpRandom))# Pop of random number and store in variable
        table_cards = []# Create a list to store the pop cards of each player
        table_cards.append(plrCard)# Append the the table cards with player card
        table_cards.append(comCard)# Append the the table cards with player card
        print("The players cards is:" , plrCard)# Show what card the player has played
        print("The computers card is:" , comCard)# Show what card the computer has played
        print("The players card count is: " , len(player))# Just to show the count of cards after pop
        print("The computers card count is: ", len(computer))# Just to show the count of cards after pop
        print("The table card count is: ", len(table_cards))# Just to show the count of cards in the table card
        if plrCard[1] > comCard[1]:# If statement to see which card is higher
            print("The player has won")
            player.extend(table_cards)# Extend the cards into players hand if won

            print("The players card count is: " , len(player))# Show new count of cards of player
            print("The computers card count is: ", len(computer))# Show new count of cards of player
        else:
            print("The computer has won")
            computer.extend(table_cards)# Extend the cards into computers hand if won

            print("The players card count is: " , len(player))# Show new count of cards of player
            print("The computers card count is: ", len(computer))# Show new count of cards of player
