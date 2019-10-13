#Create a program that calculates the amount of bugs caught using a for loop
#Sep 16, 2019
#CTI-110 - Bug Collector
#Jacob Blizzard
#

#Initialize the accumulator
Total = 0

#Ask the user for the collected amount of bugs for each day
#ALWAYS ADD 1 TO THE RANGE AS THE LIMIT WILL NOT BE INCLUDED
for day in range(1, 8):
    print("Enter the bugs collected on day", day)
    Bugs = int(input())
    Total = Total + Bugs

#Display the total bugs collected
print("You collected a total of", Total, "bugs.")
