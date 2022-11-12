###cont = True
##def functionName(parameter1, parameter2):
##    print ("do something with" + parameter1 + "and" + parameter2)
    
##cont = True
##while True:
    
import random

theNumber= random.randint(1,10)
tries = 3
playAgain = 1

def guessingGame(theNumber,playAgain):
    answer = input("Name a number 1 to 10.")
    if(int(answer) == theNumber):
        print("You're right!" + str(theNumber) + " is the answer!")
    else:
        print ("WRONG! ")
while playAgain == 1:
    while tries < 3:
        guessingGame(theNumber,playAgain)
        tries = tries + 1
    playAgain = int(input ("Type 1 to play again, 0 to exit"))
    tries = 0
