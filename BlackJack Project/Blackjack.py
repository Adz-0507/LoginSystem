import random
from Suits import *
from Suits2 import *
from CardGen import *
from PlayerCard import *
from PlayerCard2 import *
from Usersuits import *
from Usersuits2 import *

#Declaring Variables
space ="  "

Ace = int("1")
King = int("10")
Queen = int("10")
Jack = int("10")
C2 = int("2")
C3 = int("3")
C4 = int("4")
C5 = int("5")
C6 = int("6")
C7 = int("7")
C8 = int("8")
C9 = int("9")
C10 = int("10")
Blackjack = int("21")

# Getting random number
Cards = [Ace, King, Queen, Jack, C2, C3, C4, C5, C6, C7, C8, C9, C10]

random = random.choice(Cards)
cardA = random

#Printing dealers cards
print(cardA, "of", SuitA)
print(CardsB, "of", SuitB)
Cardtotal = cardA+CardsB
print(space)

if Cardtotal >Blackjack:
    print("The dealer is bust")
else:
    print("The dealers total is", Cardtotal)


#printing users cards
print(space)
print(playercard1, "of", playersuit1)
print(playercard2, "of", playersuit2)
Usertotal = playercard1+playercard2
print(space)

if Usertotal >Blackjack:
    print("You are bust")
else:
    print("Your total is", Usertotal)
    print("Would you like another card?")
    