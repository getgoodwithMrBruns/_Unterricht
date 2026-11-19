import turtle

def move(a):
     for i in range(4):
        turtle.forward(a)
        turtle.left(90)

for i in range(10):
    move(100)

turtle.done()