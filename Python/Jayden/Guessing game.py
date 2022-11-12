##Guessing Game
import random

theNumber=random.randint(1,10)

awnser = input("Pick a number between 1-10")

if (theNumber == awnser):
    print("you are right! " +theNumber+ "is the Number!")
else:
    print("sorry," + awnser + "  is incorrect! i was thinking of "+ str(theNumber) +" !" )
    
