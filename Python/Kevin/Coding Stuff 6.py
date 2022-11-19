## Turtles!
## This imports a library or module.
## Without doing this we cannot use it in code!

import turtle

## Create an instace of the turtle class
mike = turtle.Turtle()
mike.shape('turtle')
mike.color('orange')
leo = turtle.Turtle()
leo.shape('turtle')
leo.color('blue')
raph = turtle.Turtle()
raph.shape('turtle')
raph.color('red')
don = turtle.Turtle()
don.shape('turtle')
don.color('purple')


for x in range(0,4):
    leo.forward(100)
    leo.left(90)
    mike.forward(100)
    mike.right(90)
    raph.backward(100)
    raph.left(90)
    don.backward(100)
    don.right(90)
