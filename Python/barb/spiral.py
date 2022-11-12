import turtle
t=turtle.Turtle()
t.shape("turtle")
t.color("red")
count = 0
t.speed(0)
t.penup()
t.goto(0, -250)

t2=turtle.Turtle()
t2.shape("turtle")
t2.color("blue")
count2 = 0
t2.speed(0)
t2.penup()


while True:
##    t.pendown()
##    t.circle(count*5)
##    count = count + 10
##    t.penup()
##    t.goto(0,-count*5)
    t2.pendown()
    t2.forward(count2)
    t2.left(30)
    count2 = count2 + 1

    
