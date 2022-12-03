## Turtle fun
## Create a bulls eye with each turtle
import turtle

t=turtle.Turtle()
t.shape('turtle')
t.color('purple')
t.speed(99999)
some = 1

t1=turtle.Turtle()
t1.shape('turtle')
t1.color('cyan')
t1.speed(99999)
some1 = 1

t2=turtle.Turtle()
t2.shape('turtle')
t2.color('pink')
t2.speed(99999)
some2 = 1

while True:
    print(some1)
    t.forward(10 + some)
    t.right(some - 10)
    t1.forward(300 - (some1/2))
    t1.right(90)
    t2.backward((1+100)-(2*some2))
    t2.left(10*some2)
    some = some + 1
    some1 = some1 + 1
    some2 = some2 + 1
    t.backward(10 + some)
