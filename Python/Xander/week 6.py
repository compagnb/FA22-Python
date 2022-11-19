## turtles
## this imports a library or module. without doing this we cannot use it in our code

import turtle

##creating an instance of the turtle class
mike=turtle.Turtle()
mike.shape('turtle')
mike.color('orange')
leo = turtle.Turtle()
leo.shape('turtle')
leo.color('blue')
ralph = turtle.Turtle()
ralph.shape('turtle')
ralph.color('red')

##mike.forward(100)
##mike.left(90)
##mike.backward(200)
##mike.right(90)



leo.left(90)
leo.forward(90)
leo.right(90)
leo.forward(90)
leo.right(90)
leo.forward(90)
leo.right(90)
leo.forward(90)

for x in range(0,4):
    mike.forward(90)
    mike.right(90)



ralph.left(90)
ralph.forward(90)
ralph.right(90)
ralph.forward(90)
ralph.right(90)
ralph.forward(90)
ralph.right(90)
ralph.forward(90)

for x in range(0,4):
    ralph.forward(90)
    ralph.right(90)
