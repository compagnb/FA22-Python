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

#functionName("this thing", "another thing")
    
## Guessing Game with Functions
import random
theNumber=random.randint(1,10)
tries = 0
playAgain = "1"

def guessingGame(theNumber):
    ans=input("Guess the number i am thinking of between 1 and 10")
    if (int(ans) == theNumber):
        print("Correct, I was thinking of the number "+ str(theNumber) + " !")
    else:
        print("Wrong, I was thinking of the number "+ str(theNumber) + " !")

while playAgain=="1":
    while tries < 3:
        guessingGame(theNumber)
        tries = tries + 1
    playAgain = input("Type 1 to play again or 0 to exit.")
    tries = 0







