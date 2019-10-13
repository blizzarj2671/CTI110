#Sep 16, 2019
#CTI-110
#P4T1a - Shapes
#Jacob Blizzard
#

#Create Turtle
import turtle
wn = turtle.Screen()
#Rename the turtle
Minus = turtle.Turtle()

#Make the pen color clear
Minus.pencolor((1.0, 1.0, 1.0))

#From center, edges are 471
#From center, top and bottom is 396

#Get Turtle to the corner
Minus.forward(471)
Minus.right(90)
Minus.forward(396)
##Minus.right(90)
##Minus.forward(1000)

#Make the pen visible again
Minus.pencolor((0.0, 0.0, 0.0))

#Make some variables for the while loop
WLV = 1
n = 90
t = 10

#Make the while loop repeat 61 times
while WLV <= 61:
    Minus.right(n)
    Minus.forward(t)
    Minus.right(n)
    Minus.forward(t)
    Minus.right(n)
    Minus.forward(t)
    Minus.right(n)
    Minus.forward(t)
    #Add 10 to length and height and then 1 to the variable for it to stop
    t = t + 10
    WLV = WLV + 1

