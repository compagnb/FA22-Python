import turtle
kumi = turtle.Turtle()
kumi.shape("turtle")
kumi.color("purple")
for x in range(0,4):
    kumi.forward(200)
    kumi.backward(200)
    kumi.left(90)
t = turtle.Turtle()
t.shape("turtle")
t.color("blue")
t.startShape()
for x in range(0,4):
    t.forward(200)
    t.backward(200)   
    t.left(90)
t.endShape()
    
    
