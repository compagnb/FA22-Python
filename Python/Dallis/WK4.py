students = ["Dallis", "Jayden", "Terrence", "Xander","Kevin", "Skylar","Barb"]
print(students[0])
theTeacher = students[6]

answer = input ("Who is the teacher?")

if (answer == theTeacher):
    print("You are right!" +theTeacher+ " is the teacher!")
else:
    print ("Sorry," + answer + "is incorrect!")
