import turtle
import random

python= True

screen= turtle.Screen()
screen.setup(640, 420)
screen.bgpic("lvl2.gif")
screen.bgcolor("beige")

screen.addshape("portrait shaggyE.gif")

screen.addshape("shaggyE run 1 right.gif")
screen.addshape("ShaggyE run right 2.gif")
screen.addshape("Shag run right 3 .gif")

screen.addshape("shaggyE run 1 left.gif")
screen.addshape("ShaggyE run left 2.gif")
screen.addshape("ShaggyE run left.gif")

screen.addshape("kraken good.gif")

shaggy= turtle.Turtle()
shaggy.shape("portrait shaggyE.gif")
shaggy.penup()
shaggy.speed(0)
shaggy.goto(-250, 150)

kraken= turtle.Turtle()
kraken.shape("kraken good.gif")
kraken.penup()
kraken.hideturtle()
kraken.goto(230, 120)

print ("Good luck matey! Don't die to th' Kraken.")
print (" ")
print ("Go into the boat to set sail")

def right():
    python= True
    shaggy.setheading(0)
    
    x1= shaggy.xcor()
    y1= shaggy.ycor()
    
    shaggy.shape("shaggyE run 1 right.gif")
    shaggy.forward(6)
    shaggy.shape("ShaggyE run right 2.gif")
    shaggy.forward(6)
    shaggy.shape("Shag run right 3 .gif")
    shaggy.forward(6)

    if shaggy.xcor() > 20 and python==True:
        kraken.showturtle()
        print ("T'is the Kraken! Watch out! Fight it with Bluebeard's sword")
##        kraken.penup()
##        kraken.speed(5)
##        kraken.forward(20)
##        angle= random.randint(10, 350)
##        kraken.left(angle)
##        kraken.forward(20)
##        kx= kraken.xcor()
##        ky= kraken.ycor()
##        if kx < 20 or ky < 0 or kx > 320 or ky > 210:
##            kraken.forward(0)
##            kraken.left(angle)
##            kraken.forward(20)
##        python= False
    
def left():
    python= True
    shaggy.setheading(0)
    
    x1= shaggy.xcor()
    y1= shaggy.ycor()
    
    shaggy.shape("shaggyE run 1 left.gif")
    shaggy.backward(6)
    shaggy.shape("ShaggyE run left 2.gif")
    shaggy.backward(6)
    shaggy.shape("ShaggyE run left.gif")
    shaggy.backward(6)

    if shaggy.xcor() > 20 and python== True:
        kraken.showturtle()
        print ("T'is the Kraken! Watch out! Fight it with Bluebeard's sword")
##        kraken.penup()
##        kraken.speed(5)
##        kraken.forward(20)
##        angle= random.randint(10, 350)
##        kx= kraken.xcor()
##        ky= kraken.ycor()
##        if kx < 20 or ky < 0 or kx > 320 or ky > 210:
##            kraken.forward(0)
##            kraken.left(angle)
##            kraken.forward(20)
##        python= False
    
def up():
    python= True
    shaggy.setheading(90)
    
    x1= shaggy.xcor()
    y1= shaggy.ycor()
    
    shaggy.shape("shaggyE run 1 left.gif")
    shaggy.forward(6)
    shaggy.shape("ShaggyE run left 2.gif")
    shaggy.forward(6)
    shaggy.shape("ShaggyE run left.gif")
    shaggy.forward(6)

    if shaggy.xcor() > 20 and python== True:
        kraken.showturtle()
        print ("T'is the Kraken! Watch out! Fight it with Bluebeard's sword")
##        kraken.penup()
##        kraken.speed(5)
##        kraken.forward(20)
##        angle= random.randint(10, 350)
##        kx= kraken.xcor()
##        ky= kraken.ycor()
##        if kx < 20 or ky < 0 or kx > 320 or ky > 210:
##            kraken.forward(0)
##            kraken.left(angle)
##            kraken.forward(20)
##        python= False
    
def down():
    python= True
    shaggy.setheading(270)

    x1= shaggy.xcor()
    y1= shaggy.ycor()
    
    shaggy.shape("shaggyE run 1 right.gif")
    shaggy.forward(6)
    shaggy.shape("ShaggyE run right 2.gif")
    shaggy.forward(6)
    shaggy.shape("Shag run right 3 .gif")
    shaggy.forward(6)

    if shaggy.xcor() > 20 and python== True:
        kraken.showturtle()
        print ("T'is the Kraken! Watch out! Fight it with Bluebeard's sword")
##        kraken.penup()
##        kraken.speed(5)
##        kraken.forward(20)
##        angle= random.randint(10, 350)
##        kx= kraken.xcor()
##        ky= kraken.ycor()
##        if kx < 20 or ky < 0 or kx > 320 or ky > 210:
##            kraken.forward(0)
##            kraken.left(angle)
##            kraken.forward(20)
##        python= False
    
screen.onkey(right, "Right")
screen.onkey(left, "Left")
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.listen()

screen.onclick(shaggy.goto)

#kraken.setheading(kraken.towards(shaggy))

##while python== True:
##    kraken.penup()
##    kraken.speed(5)
##    kraken.forward(20)
##    angle= random.randint(10, 350)
##    kx= kraken.xcor()
##    ky= kraken.ycor()
##    if kx < 20 or ky < 0:
##        kraken.left(angle)
##    python= False
