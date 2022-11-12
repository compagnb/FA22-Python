import turtle

t= turtle.Turtle()
t.shape("turtle")
t.color("red")
count = 0
t.speed(0)

t2= turtle.Turtle()
t2.shape("turtle")
t2.color("blue")
count1 = 10
t2.speed(0)

t3= turtle.Turtle()
t3.shape("turtle")
t3.color("green")
count2 = 20
t3.speed(0)

t4= turtle.Turtle()
t4.shape("turtle")
t4.color("yellow")
count3 = 100
t4.speed(0)


while True:
    t.forward(count +10)
    t.left(count + 5)
    t2.forward(count1 -10)
    t2.right(count1 - 5)
    t3.forward(count2 * 5)
    t3.left(count2 * 5)
    t4.forward(count3 / 5)
    t4.right(count3 / 5)
    count = count + 1
    count1 = count * 2    
    count2 = count + 3
    count3 = count * 4
