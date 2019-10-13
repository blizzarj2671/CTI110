#CTI-110
#P3T1 - Areas Of Rectangles
#Jacob Blizzard
#Sep 9, 2019
#

#Input the length and width of rectangle 1
length1 = int(input("Enter the length of rectangle 1: "))
width1 = int(input("Enter the width of rectangle 1: "))

#Input the length and width of rectangle 2
length2 = int(input("Enter the length of rectangle 2: "))
width2 = int(input("Enter the width of rectangle 2: "))

#Calculate the area of rectangle 1
area1 = length1 * width1

#Calculate the area of rectangle 2
area2 = length2 * width2

#Determine which area is bigger using if elif statement
if area1 > area2:
    print("Rectangle 1 has the greater area")
#"Else if" is elif
elif area2 > area1:
    print("Rectangle 2 has the greater area")
#If none are bigger, they are the same
else:
    print("Both rectangles have the same area")
#Nested else if statements look like this:
#if area1 > area2:
    #print("Rectangle 1 has the greater area")
#else:
    #if area2 > area1:
        #print("Rectangle 2 has the greater area")
    #else:
        #print("Both rectangles have the same area")
