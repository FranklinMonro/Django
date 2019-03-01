import random

SUITE = 'H D S C'.split()# Create the suits list
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()# Create the ranks list

DECKS = [(s,r) for s in SUITE for r in RANKS]# Create the decks

random.shuffle(DECKS)# Shuffle the decks

player = DECKS[:26]# split deck evenly
computer = DECKS[26:]# split deck evenly





while len(player) != 0 or len(computer) != 0:
        print("The players card count is: " , len(player))
        print("The computers card count is: ", len(computer))
        plrRandom = random.randint(0, len(player)-1)
        cmpRandom = random.randint(0, len(computer)-1)
        plrCard = player.pop((plrRandom))
        comCard = computer.pop((cmpRandom))
        table_cards = []
        table_cards.append(plrCard)
        table_cards.append(comCard)
        print("The players cards is:" , plrCard)
        print("The computers card is:" , comCard)
        print("The players card count is: " , len(player))
        print("The computers card count is: ", len(computer))
        print("The table card count is: ", len(table_cards))
        if plrCard[1] > comCard[1]:
            print("The player has won")
            player.extend(table_cards)

            print("The players card count is: " , len(player))
            print("The computers card count is: ", len(computer))
        else:
            print("The computer has won")
            computer.extend(table_cards)

            print("The players card count is: " , len(player))
            print("The computers card count is: ", len(computer))
