cont = True
import random
    #Numbers = ["1","2","3","4","5","6","7","8","9","10"]
theNumber= random.randint(1,10)
while cont == True:
    answer = input ("Name a number 1 to 10.")
    if(answer == theNumber):
        print("You're right!" + theNumber + " is the answer!")
    else:
        print ("WRONG!")
