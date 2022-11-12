##Guessing Game
import random
tries=0
retry = 'yes'
theNumber=random.randint(1,9)
while retry =='yes':
    while tries < 3:
        answer = input("What single-digit number am i thinking of?")
        if (answer == str(theNumber)):
            print("You got it! I was thinking of "+ str(theNumber) + "!")
        else:
            tries = tries + 1
            print("No, that's not it!")
        retry = input("type 'yes' to play again.")
    

