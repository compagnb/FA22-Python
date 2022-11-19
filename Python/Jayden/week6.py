## Turtles!

## this imports a library or mdule.
##Without doing this we cannot use it in our code!
import turtle

##Creating an instance of the turtle class
leonardo = turtle.Turtle()
leonardo.shape('turtle')
leonardo.color('blue')

##leonardo.forward(100)
##leonardo.left(90)
##leonardo.backward(200)
##leonardo.right(90)

mike = turtle.Turtle()
mike.shape('turtle')
mike.color('orange')

mike.forward(105)
mike.left(90)
mike.forward(105)
mike.left(90)
mike.forward(105)
mike.left(90)
mike.forward(105)

for x in range(0,4):
    leonardo.forward(105)
    leonardo.right(90)
    print(x)

ralph = turtle.Turtle()    
ralph.shape('turtle')
ralph.color('red')

##ralph.backward(100)
##ralph.left(90)
##ralph.backward(200)
##ralph.right(90)

donn = turtle.Turtle()
donn.shape('turtle')
donn.color('purple')

donn.left(90)
donn.forward(105)
donn.left(90)
donn.forward(105)
donn.left(90)
donn.forward(105)
donn.left(90)
donn.forward(105)

for x in range(0,4):
    ralph.backward(105)
    ralph.left(90)
    print(x)


