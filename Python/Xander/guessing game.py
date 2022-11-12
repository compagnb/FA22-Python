# Guessing Game
import random

theNumber=random.randint(1,10)

while True:
    answer = input("what nummber am i thinking of between 1 and 10?")
    if (int(answer) == theNumber):
        print("you are phycic! " + str(theNumber) +  "is the number!")
    else:
        print("wrong, i was thinking of the number "+ str(theNumber) + " !")
