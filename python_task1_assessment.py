
import random #import random
digits = list(range(10)) #create list of number from 0 - 9 and add to a list
random.shuffle(digits)#shuffle the numbers randomly
print(digits[:3])#print out the 3 digits


guessInput = input("What is your guess? ")#get input fromuser
guessList = list(guessInput)#put numbers into a list
guess = [int(i) for i in guessList]#make string into intergers
print(guess)#print out guess

def close(guess):#function to check if a number is in the digits list

    if guess[:1] == digits[:1] or guess[:1] == digits[1:2] or guess[:1] == digits[2:3]:
        close_result = "You have a number correct in list"
    elif guess[1:2] == digits[:1] or guess[1:2] == digits[1:2] or guess[1:2] == digits[2:3]:
        close_result = "You have a number correct in list"
    elif guess[2:3] == digits[:1] or guess[2:3] == digits[1:2] or guess[2:3] == digits[2:3]:
        close_result = "You have a number correct in list"
    else:
        result = "You have no number correct in list"

    return close_result
close_result = close(guess)

def match(guess):#function to check if a number is in a correct spot

    if guess[:1] == digits[:1]:
        match_result = "You got a number correct in the correct spot as well"
    elif guess[1:2] == digits[1:2]:
        match_result = "You got a number correct in the correct spot as well"
    elif gues[2:3] == digits[2:3]:
        match_result = "You got a number correct in the correct spot as well"
    else:
        match_result = "You got no number correct in the correct spot as well"

    return match_result
match_result = match(guess)

def win(guess):#function to check if guess is correct
    if guess[:3] == digits[:3]:
        win_result = "You Win"
    else:
        win_result = "Try Again"

    return win_result
win_result = win(guess)

print(close_result)
print(match_result)
print(win_result)

while win_result != "You Win":
    guessInput = input("What is your guess? ")#get input fromuser
    guessList = list(guessInput)#put numbers into a list
    guess = [int(i) for i in guessList]#make string into intergers
    print(guess)
    if win_result == "You Win":
        print(win_result)
    else:
        print("Try again")
