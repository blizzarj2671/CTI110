#Make a program that does a staircase with a wall using a nested loop
#Sep 23, 2019
#CTI-110 P4HW3 - Nested Loops
#Jacob Blizzard
#

##Make a program that draws a diagnol line and a straight line on the same row
##Use a nested loop and make it look like so
##
# #
#  #
#   #
#    #
#     #

#Make sure there is only one row
for r in range(1,2):
    #Put in six columns
    for c in range(1,7):
        #Put in the straight line of "#"
        print("#", end = "")
        #Put in the diagnol line in "#" based on the c columns
        for r in range(c):
            #Make sure the lines are diagnol
            print(" ", end = "")
        print("#")
        
