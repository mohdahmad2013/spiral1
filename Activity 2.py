import turtle
turtle.Screen().bgcolor("red")
turtle.Screen().setup(500,500)
mypen=turtle.Turtle()
s=0
while True:
    for i in range (4):
        mypen.fd(s+1)
        mypen.left(90)
        s=s-5
    s=s+1