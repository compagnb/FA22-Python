## Week 2
## Scary Madlibs
## print story and with user input
##
## Variable Rules
## Cannot start with capital letters
## Cannot start with numbers
## Cannot contain special characters like ?!.
## Cannot have spaces in them - use body-part bodyPart 
## Cannot have the same name as other variables

noun = input("Enter a noun.")
adj = input("Enter an adjective.")
verbing = input("Enter a verb using -ing.")
adj2 = input("Enter an adjective.")
verb = input("Enter a verb.")
bodyPart = input("Enter a body part.")
verb2 = input("Enter a verb.")
verb3 = input("Enter a verb.")
adj3 = input("Enter an adjective.")
bodyPart2 = input("Enter a body part (Plural).")
color = input("Enter a color.")
animal = input("Enter an animal (Plural).")
color2 = input("Enter a color.")
beverage = input("Enter a beverage.")
adj4 = input("Enter an adjective.")               
bodyPart3 = input("Enter a body part (Plural).")

story = "Did you know there's going to be a "+noun+" at the "+adj+" School for Zombies? There will be a DJ "+verbing+" "+adj2+" songs to "+verb+" to. Popular zombie dances include The "+bodyPart+" "+verb2+" and The "+verb3+". The school gym is decorated with"+adj3+" "+bodyPart2+"and "+color+" "+animal+" heads. In between songs, there aretreats like"+color2+" "+beverage+" and "+adj4+" "+bodyPart3+"."

print(story)

