##FUNCTIONS
##Functions are pieces of reusable code
##
##count = 0
##def functionName(parameter1, parameter2):
##    print("do something with " + parameter1 + " and " + parameter2)
##
##while count<100:
##    functionName("this", "that")
##    count = count +1
##    
##functionName("this thing", "another thing")
##

import random

theNumber=random.randint(1,10)
def guessingGame(theNumber):
    tries = 0
    ans=input("Guess the Number i am thinking of between 1 and 10")
    
    if (theNumber == ans):
        print("you are right! " +theNumber+ "is the Number!")
    else:
        print("sorry," + ans + "  is incorrect! i was thinking of "+ str(theNumber) +" !" )
    
while playAgain=="1":
    while tries < 3:
       guessingGame(theNumber,playAgain)
       tries = tries + 1
    playAgain = input("Type 1 to play again or 0 to exit.")  
    tries = 0





