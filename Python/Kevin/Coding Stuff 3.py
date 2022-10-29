## Week 3
## Lists can contain a bunch of variables
## ints, floats, chars, strings

numOfHouses=0

trickOrTreatBag = []

while numOfHouses <= 10:
    treat = input("Trick or Treat! Give me something good to eat!")
    trickOrTreatBag.append(treat)
    print(trickOrTreatBag)
    eatNow = input("Do you want to eat this now?")
    print (numOfHouses)
    if eatNow=="yes":
        del trickOrTreatBag[numOfHouses]
    numOfHouses = numOfHouses + 1
print("Wow, we wnt to " + numOfHouses + "! Can't wait for next halloween!")
