#Write a program to create graphics with turtle.
#September 4, 2019.
#CTI-110 P2HW2- Turtle Graphic
#Jacob Blizzard
#

#Create Turtle
import turtle
wn = turtle.Screen()
#Rename the turtle
Minus = turtle.Turtle()
#Make the drawing more noticable
Minus.pensize(6.1)

#Make the first square
Minus.forward(90)
Minus.left(90)
Minus.forward(90)
Minus.left(90)
Minus.forward(90)
#Make the center line
Minus.left(135)
Minus.forward(254)
Minus.left(135)
#Make the second square
Minus.forward(90)
Minus.left(90)
Minus.forward(90)
#Finish the first square
Minus.right(90)
Minus.forward(90)
Minus.left(90)
Minus.forward(90)
Minus.left(90)
Minus.forward(90)
Minus.left(90)
Minus.forward(90)
#Finish the second square
Minus.right(90)
Minus.forward(90)
Minus.left(90)
Minus.forward(90)
Minus.left(90)
Minus.forward(90)
#Make the rightmost outer line
Minus.left(45)
Minus.forward(127)
Minus.left(45)
Minus.forward(90)
Minus.left(90)
Minus.forward(90)
#Make the leftmost outer line
Minus.left(45)
Minus.forward(127)
#Finish the drawing
Minus.left(45)
Minus.forward(90)
Minus.left(135)
Minus.forward(254)
