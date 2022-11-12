## Week 4
## Conditionals are "if this, then that"

students = ['Dallis', 'Jayden', 'Terrence', 'Xander', 'Kevin', 'Skylar', 'Barb']
theBest = students[len(students)-1]

answer = input("Who is the best in this class?")

if answer == theBest:
    print("You are right! " + theBest + " is the best!")
else:
    print("Sorry, "+ answer + " is not the best!")
