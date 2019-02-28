import random

SUITE = 'H D S C'.split()# Create the suits list
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()# Create the ranks list

DECKS = [(s,r) for s in SUITE for r in RANKS]# Create the decks

random.shuffle(DECKS)# Shuffle the decks

player = DECKS[:26]# split deck evenly
computer = DECKS[26:]# split deck evenly
print("The players card count is: " , len(player))
print("The computers card count is: ", len(computer))
plrCard = player.pop()
comCard = computer.pop()
table_cards = []
table_cards.append(plrCard)
table_cards.append(comCard)
#player = input("Please enter your name: ")

print("The players cards is:" , plrCard)
print("The computers card is:" , comCard)


if plrCard[1] == comCard[1]:
    print("this is war!")
elif plrCard[1] > comCard[1]:
    print("The player has won")
    player.append(table_cards)
    print("The players card count is: " , len(player))
    print("The computers card count is: ", len(computer))
else:
    print("The computer has won")
    computer.append(table_cards)
    print("The players card count is: " , len(player))
    print("The computers card count is: ", len(computer))
