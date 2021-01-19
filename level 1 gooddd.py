#current tasks-if shaggy touches enemy, lose health; make shaggy fight; stop shaggy from crossing over edges;
#make the treasure open and change shaggy's look; create ending message; add more enemies?

import turtle
import math
import time #not needed?
import random
python= False

screen= turtle.Screen()
screen.setup(680, 430)
screen.bgpic("beach.gif")
screen.addshape("shaggy best.gif")
screen.addshape("old man.gif")
screen.addshape("cave.gif")
screen.title("Coral Bay Invasion")
screen.bgcolor("beige") 

screen.addshape("shaggy run 1 right.gif")
screen.addshape("shaggy run 2 right.gif")
screen.addshape("shaggy run 3 right.gif")

screen.addshape("shaggy run 1 left.gif")
screen.addshape("shaggy run 2 left.gif")
screen.addshape("shaggy run 3 left.gif")

screen.addshape("Skelly left.gif")
screen.addshape("Skelly right.gif")
screen.addshape("Ghost.gif")
screen.addshape("Ghost inverted.gif")

screen.addshape("treasure 1.gif")
screen.addshape("treasure 2.gif")

screen.addshape("shaggyE run 1 right.gif")
screen.addshape("ShaggyE run right 2.gif")
screen.addshape("Shag run right 3 .gif")

screen.addshape("shaggyE slash 1.gif")
screen.addshape("shaggyE slash 2.gif")
screen.addshape("shaggyE slash 3.gif")

screen.addshape("shaggyE slash 4.gif")
screen.addshape("shaggyE slash 4.gif")
screen.addshape("shaggyE slash 6.gif")

screen.addshape("shaggyE run 1 left.gif")
screen.addshape("shaggyE run left 2.gif")
screen.addshape("ShaggyE run left.gif")

shaggy=turtle.Turtle()
shaggy.shape("shaggy best.gif")
shaggy.shapesize(10) 
shaggy.penup()
shaggy.speed(3)
shaggy.goto(0, 150) 
shaggy.penup()

oldman=turtle.Turtle()
oldman.shape("old man.gif")
oldman.speed(0)
oldman.shapesize(3)
oldman.penup()
oldman.goto(170, 0)

leftskelly=turtle.Turtle()
leftskelly.shape("Skelly left.gif")
leftskelly.hideturtle()

leftskelly2=turtle.Turtle()
leftskelly2.shape("Skelly left.gif")
leftskelly2.hideturtle()

ghost1= turtle.Turtle()
ghost1.shape("Ghost.gif")
ghost1.hideturtle()

ghost2= turtle.Turtle()
ghost2.shape("Ghost inverted.gif")
ghost2.hideturtle()

ghost3= turtle.Turtle()
ghost3.shape("Ghost.gif")
ghost3.hideturtle()

treasure_chest= turtle.Turtle()
treasure_chest.shape("treasure 1.gif")
treasure_chest.hideturtle()
treasure_chest.penup()
treasure_chest.goto(140, -150)

print ("Ahoy matey! Welcome to Coral Bay. The people are in desperate need of someone who can defeat the Kraken.")
print ("The Kraken invades every 30 years and has only nearly been defeated by the legend, Bluebeard.")
print ("Walk to towards the old man to begin your quest")

print(" ")
health= 5
print ("Health: 5")

#count= 0

def narration(): #old man talking
    count = 0
    x1= shaggy.xcor()
    y1= shaggy.ycor()
    x2= oldman.xcor()
    y2= oldman.ycor()
    d= math.sqrt((x2-x1)**2 + (y2-y1)**2)
    python= True
    if d < 30:
        print (" ")
        print ("Hey boy, I have a task for ye. We here at Coral Bay need someone to fight th' Kraken.")
        print ("Look for Bluebeard's treasure. Legend has it, he left behind his sword, his hat, and potions.")
        print ("Go into this cave 'ere. Beware of th' skellies!")

def cave():
    python= True
    x1= shaggy.xcor()
    y1= shaggy.ycor()
    x3= 0
    y3= -72
    d2= math.sqrt((x3-x1)**2 + (y3- y1)**2)
    angle=random.randint(10, 350)
    angle2=random.randint(10, 350)
    angle3=random.randint(10, 350)
    if d2 < 30: #cave entrance coor ->(0, - 72)
        x3= 1000
        y3= 1000
        screen.setup(800, 800)
        screen.bgpic("cave.gif")
        screen.bgcolor("black")
        oldman.hideturtle()
        shaggy.goto(-50, 320)
        oldman.clear()
        leftskelly.penup()
        leftskelly.goto(-265, 130)
        leftskelly.showturtle()

        leftskelly2.penup()
        leftskelly2.goto(30, -60)
        leftskelly2.showturtle()

        while python== True:
        
            ghost1.showturtle()
            ghost1.penup()
            ghost1.speed(3)
            ghost1.forward(20)
            ghostx= ghost1.xcor()
            ghosty= ghost1.ycor()
            if ghostx <= -300 or ghostx >= 300 or ghosty <= - 300 or ghosty >= 300:
                ghost1.left(angle)
                
            ghost2.showturtle()
            ghost2.penup()
            ghost2.speed(3)
            ghost2.backward(20)
            ghost2x= ghost2.xcor()
            ghost2y= ghost2.ycor()
            if ghost2x <= -300 or ghost2x >= 300 or ghost2y <= - 300 or ghost2y >= 300:
                ghost2.left(angle2)
                
            ghost3.showturtle()
            ghost3.penup()
            ghost3.speed(3)
            ghost3.forward(20)
            ghost3x= ghost3.xcor()
            ghost3y= ghost3.ycor()
            if ghost3x <= -300 or ghost3x >= 300 or ghost3y <= - 300 or ghost3y >= 300:
                ghost3.left(angle3)
                
            #health()
            #python= False
            loot_room()
        
def health():
    health= 5
    x1= shaggy.xcor()
    y1= shaggy.ycor()

    x4= leftskelly.xcor()
    y4= leftskelly.ycor()
    d4= math.sqrt((x4-x1)**2 + (y4-y1)**2)

    x8= leftskelly2.xcor()
    y8= leftskelly2.ycor()
    d8= math.sqrt((x8-x1)**2 + (y8-y1)**2)

    x9= ghost1.xcor()
    y9= ghost1.ycor()
    d9= math.sqrt((x9-x1)**2 + (y9-y1)**2)

    x10= ghost2.xcor()
    y10= ghost2.ycor()
    d10= math.sqrt((x10-x1)**2 + (y10-y1)**2)

    x11= ghost3.xcor()
    y11= ghost3.ycor()
    d11= math.sqrt((x11-x1)**2 + (y11-y1)**2)

    if d4 < 20 or d8 < 20 or d9 < 20 or d10 < 20 or d11 < 20:
        health= health - 1
        print ("Health:", health)
    
def loot_room():
    x1=shaggy.xcor()
    y1=shaggy.ycor()
    x5= -50
    y5= -350
    d5= math.sqrt((x5-x1)**2 + (y5- y1)**2)
    if d5 < 20:
        leftskelly.hideturtle()
        ghost1.hideturtle()
        ghost2.hideturtle()
        ghost3.hideturtle()
        
        screen.bgpic("loot room.gif")
        screen.setup(700, 650)
        screen.bgcolor("beige")
        shaggy.speed(0)
        shaggy.goto(0, 140)
        
        treasure_chest.showturtle()
         
def treasure():
    variable= 0
    x1=shaggy.xcor()
    y1=shaggy.ycor()
    x6= 140
    y6= -150
    d6= math.sqrt((x6-x1)**2 + (y6-y1)**2)
    if d6 < 30:
        treasure_chest.shape("treasure 2.gif")
        shaggy.shape("shaggyE run 1 right.gif")      
        def right2(): 
            shaggy.setheading(0)
            count= 0
            x1= shaggy.xcor()
            y1= shaggy.ycor()
            x2= oldman.xcor()
            y2= oldman.ycor()
            narration()
            shaggy.shape("shaggyE run 1 right.gif")
            shaggy.forward(6)
            shaggy.shape("ShaggyE run right 2.gif")
            shaggy.forward(6)
            shaggy.shape("Shag run right 3 .gif")
            shaggy.forward(6)
            cave()          
            loot_room()
            #health()
            treasure()  
            python= False
        def left2():
            shaggy.setheading(0)
            count= 0
            x1= shaggy.xcor()
            y1= shaggy.ycor()
            x2= oldman.xcor()
            y2= oldman.ycor()
            narration()
            shaggy.shape("shaggyE run 1 left.gif")
            shaggy.backward(6)
            shaggy.shape("shaggyE run left 2.gif")
            shaggy.backward(6)
            shaggy.shape("ShaggyE run left.gif")
            shaggy.backward(6)
            cave()       
            loot_room()
            #health()
            treasure()
            python= False
        def up2():
            shaggy.setheading(90)
            count= 0
            x1= shaggy.xcor()
            y1= shaggy.ycor()
            x2= oldman.xcor()
            y2= oldman.ycor()
            narration()
            shaggy.shape("shaggyE run 1 left.gif")
            shaggy.forward(6)
            shaggy.shape("shaggyE run left 2.gif")
            shaggy.forward(6)
            shaggy.shape("ShaggyE run left.gif")
            shaggy.forward(6)
            cave()
            loot_room()
            #health()
            treasure()
            python= False
        def down2():
            shaggy.setheading(270)
            count= 0
            x1= shaggy.xcor()
            y1= shaggy.ycor()
            x2= oldman.xcor()
            y2= oldman.ycor()
            narration()
            shaggy.shape("shaggyE run 1 right.gif")
            shaggy.forward(6)
            shaggy.shape("ShaggyE run right 2.gif")
            shaggy.forward(6)
            shaggy.shape("Shag run right 3 .gif")
            shaggy.forward(6)
            cave()                      
            loot_room()
            #health()
            treasure()
            python= False
        screen.onkey(right2, "Right")
        screen.onkey(left2, "Left")
        screen.onkey(up2, "Up")
        screen.onkey(down2, "Down")
        screen.listen()
        print (" ")
        print ("Congratulations, matey! You have found Bluebeard's hidden treasure. Time to fight the Kraken.")
            
def right(): 
    shaggy.setheading(0)
    count= 0
    x1= shaggy.xcor()
    y1= shaggy.ycor()
    x2= oldman.xcor()
    y2= oldman.ycor()
    
    narration()
    
    shaggy.shape("shaggy run 1 right.gif")
    shaggy.forward(6)
    shaggy.shape("shaggy run 2 right.gif")
    shaggy.forward(6)
    shaggy.shape("shaggy run 3 right.gif")
    shaggy.forward(6)

    cave()
                
    loot_room()

    #health()

    treasure()  
    
    python= False
    
def left():
    shaggy.setheading(0)
    count= 0
    x1= shaggy.xcor()
    y1= shaggy.ycor()
    x2= oldman.xcor()
    y2= oldman.ycor()
    
    narration()
    
    shaggy.shape("shaggy run 1 left.gif")
    shaggy.backward(6)
    shaggy.shape("shaggy run 2 left.gif")
    shaggy.backward(6)
    shaggy.shape("shaggy run 3 left.gif")
    shaggy.backward(6)
    
    cave()
                
    loot_room()

    #health()
    
    treasure()
    
    python= False

def up():
    shaggy.setheading(90)
    count= 0
    x1= shaggy.xcor()
    y1= shaggy.ycor()
    x2= oldman.xcor()
    y2= oldman.ycor()
    
    narration()
    
    shaggy.shape("shaggy run 1 left.gif")
    shaggy.forward(6)
    shaggy.shape("shaggy run 2 left.gif")
    shaggy.forward(6)
    shaggy.shape("shaggy run 3 left.gif")
    shaggy.forward(6)
    
    cave()
    
    loot_room()

    #health()

    treasure()
    
    python= False

def down():
    shaggy.setheading(270)
    count= 0
    x1= shaggy.xcor()
    y1= shaggy.ycor()
    x2= oldman.xcor()
    y2= oldman.ycor()
    
    narration()
    
    shaggy.shape("shaggy run 1 right.gif")
    shaggy.forward(6)
    shaggy.shape("shaggy run 2 right.gif")
    shaggy.forward(6)
    shaggy.shape("shaggy run 3 right.gif")
    shaggy.forward(6)

    cave()
                
    loot_room()

    #health()

    treasure()
    
    python= False

##def slashR():
##    shaggy.shape("shaggyE slash 1.gif")
##    time.sleep(0.1)
##    shaggy.shape("shaggyE slash 2.gif")
##    time.sleep(0.1)
##    shaggy.shape("shaggyE slash 3.gif")
    #reverse = 1
    #time.sleep(0.2)
    #kraken_damage()
    #shaggy_death()
    #kraken_death()
    #kraken_ten()
    
##def slashL():
##    shaggy.shape("shaggyE slash 4.gif")
##    time.sleep(0.1)
##    shaggy.shape("shaggyE slash 5.gif")
##    time.sleep(0.1)
##    shaggy.shape("shaggyE slash 6.gif")
    #reverse = 1
    #time.sleep(0.2)
    #reverse = 0
    #kraken_damage()
    #shaggy_death()
    #kraken_death()
    #kraken_ten()

screen.onkey(right, "Right")
screen.onkey(left, "Left")
screen.onkey(up, "Up")
screen.onkey(down, "Down")
#screen.onkey(slashR, "R")
#screen.onkey(slashL, "E")

screen.listen()

x2= 1000
y2= 1000



