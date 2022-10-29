#doYouWantToContinue = True
numOfHouses = 0
trickOrTreatBag = []
#while doYouWantToContinue == True:
while numOfHouses <= 10 :
    treat = input ("Trick or treat! Give me something good to eat!")
    trickOrTreatBag.append(treat)
    print(trickOrTreatBag)
    eatNow = input ("Would you like to eat this now? Type yes or no.")
    if eatNow == "yes":
         trickOrTreatBag.remove(numOfHouses)
    numOfHouses = numofHouses + 1
print (" We went to" + numOfHouses + ", and I am pooped!")
