#CTI-110
#P3HW1 - Month Number
#Jacob Blizzard
#Sep 9, 2019
#

#Ask for the number
MonthNumber = int(input("Enter the number of the month: "))

#Make the error message
if MonthNumber > 12:
    print("Error: Number cannot be higher than 12")
elif 1 > MonthNumber:
    print("Error: Number cannot be lower than 1")

#Display the month name
elif MonthNumber == 1:
        print("Janurary")
elif MonthNumber == 2:
        print("Feburary")
elif MonthNumber == 3:
        print("March")
elif MonthNumber == 4:
        print("April")
elif MonthNumber == 5:
        print("May")
elif MonthNumber == 6:
        print("June")
elif MonthNumber == 7:
        print("July")
elif MonthNumber == 8:
        print("August")
elif MonthNumber == 9:
        print("September")
elif MonthNumber == 10:
        print("October")
elif MonthNumber == 11:
        print("November")
elif MonthNumber == 12:
        print("December")
