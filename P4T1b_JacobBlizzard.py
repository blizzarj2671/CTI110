#Sep 16, 2019
#CTI-110
#P4T1b - Initials
#Jacob Blizzard
#

#Create Turtle
import turtle

#Rename the turtle, make the pen clear
Echo = turtle.Turtle()
Echo.pencolor((1.0, 1.0, 1.0))

#Get the turtle to the start of my first initial
Echo.right(180)
Echo.forward(100)
Echo.right(90)
Echo.forward(100)

#Make the turtle visible now and increase size
Echo.pencolor((0.0, 1.0, 1.0))
Echo.pensize(2.7)

#Start drawing the J
Echo.right(90)
Echo.forward(127)
Echo.right(180)
Echo.forward(63.5)
Echo.left(90)
Echo.forward(127)

#Draw the loop of the J
ELV = 1
while ELV <= 12:
    Echo.right(15)
    Echo.forward(10)
    ELV = ELV + 1

#Get to the position of B
Echo.pencolor((1.0, 1.0, 1.0))
Echo.forward(117)
Echo.right(90)
Echo.forward(5)
Echo.pencolor((0.0, 1.0, 1.0))
Echo.forward(135)
Echo.pencolor((1.0, 1.0, 1.0))
Echo.forward(45)

#Start drawing the B
Echo.pencolor((0.0, 1.0, 1.0))
Echo.right(90)
Echo.forward(157)
Echo.left(90)
Echo.forward(75)

#Create the first loop of B
ELV = 1
while ELV <= 12:
    Echo.left(15)
    Echo.forward(11)
    ELV = ELV + 1

#Get the the starting point of the second loop
Echo.forward(64)
Echo.right(90)
Echo.forward(72)
Echo.right(90)
Echo.forward(75)

#Create the second loop of B
ELV = 1
while ELV <= 12:
    Echo.right(15)
    Echo.forward(9.45)
    ELV = ELV + 1
Echo.forward(69)

#Create the second turtle
import turtle
Dark = turtle.Turtle()
Dark.pencolor((1.0, 1.0, 1.0))
Dark.forward(11)
Dark.right(90)
Dark.forward(11)
Dark.left(90)

#Get the turtle to the second starting point of the J
Dark.right(180)
Dark.forward(100)
Dark.right(90)
Dark.forward(100)

#Set the color and pensize
Dark.pencolor((0.5, 0.0, 1.0))
Dark.pensize(2.7)

#Start the drawing of the J
Dark.right(90)
Dark.forward(127)
Dark.right(180)
Dark.forward(63.5)
Dark.left(90)
Dark.forward(127)

#Create the loop on the J
DLV = 1
while DLV <= 12:
    Dark.right(15)
    Dark.forward(10)
    DLV = DLV + 1

#Get to the starting point of B 2
#DONT ERASE PART OF THE FIRST B
Dark.pencolor((1.0, 1.0, 1.0))
Dark.forward(117)
Dark.right(90)
Dark.forward(5)
Dark.pencolor((0.5, 0.0, 1.0))
Dark.forward(135)
Dark.pencolor((1.0, 1.0, 1.0))
Dark.forward(33)
Dark.pencolor((0.0, 1.0, 1.0))
Dark.forward(2.7)
Dark.pencolor((1.0, 1.0, 1.0))
Dark.forward(9.3)

#Start drawing the second B
Dark.pencolor((0.5, 0.0, 1.0))
Dark.right(90)
Dark.forward(157)
Dark.left(90)
Dark.forward(75)

#Make the first loop on the B
DLV = 1
while DLV <= 12:
    Dark.left(15)
    Dark.forward(11)
    DLV = DLV + 1

#Get to the second loop's starting point
Dark.forward(64)
Dark.right(90)
Dark.forward(72)
Dark.right(90)
Dark.forward(75)

#Draw the second loop and finish the drawing
DLV = 1
while DLV <= 12:
    Dark.right(15)
    Dark.forward(9.45)
    DLV = DLV + 1
Dark.forward(69)
