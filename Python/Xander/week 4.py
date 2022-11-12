## WEEK 4
## CONDITIONALS
## if this then that

pokemon = ['grookey', 'pikachu', 'eevee', 'squirtle', 'mewtwo', 'umbreon', 'Zacian', 'mew']
theBest = pokemon[0]

answer = input("who is the best pokemon?")

if (answer == theBest):
    print("you are right! " +theBest+  "is the best!")
else:
    print("sorry, "+ answer + "  is incorrect.")
