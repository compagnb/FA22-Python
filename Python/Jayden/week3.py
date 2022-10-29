## Week 3
## LIST - can contain a bunch of variable
## ints, floats, chars, strings

numOfHouses=0

doYouWantToContinue=True

trickOrTreatBag = ['twix', 'chocolate covered no', 'family sized bag of chips', 'chocolate covered chucky bar',]

while numOfHouses <= 10:
    treat = input("Trick or treat! Give me somthing good to eat.")
    trickOrTreatBag.append(treat)
    print(trickOrTreatBag)
    eatNow = input("Do you want to eat this now? type yes or no")
    if eatNow=="yes":
        trickOrTreatBag.remove(numOfHouses)
    numOfHouses = numOfHouses + 1
print("Wow, we went to " + numOfHouses + ", and I am pooped!")
    
    
