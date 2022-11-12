##Guessing Game
import random

theNumber=random.randint(1,10)
ans=input("Guess the number i am thinking of between 1 and 10")

if (ans == theNumber):
    print("Correct, I was thinking of the number "+ str(theNumber) + " !")
else:
    print("Wrong, I was thinking of the number "+ str(theNumber) + " !")
