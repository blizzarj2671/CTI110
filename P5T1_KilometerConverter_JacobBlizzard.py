#Create program that asks the user to put in a distance in kilometers which gets converted into miles
#Sep 24, 2019
#CTI-110 P5T1_KilometerConverter
#Jacob Blizzard
#

##kilometers = float(input("How many kilometers?: "))
##miles = kilometers * .6214
##print("Miles: ", format(miles, ",.2f")

#Number to convert kilometers to miles
conversionfactor = .6214

#The main function gets a distance in kilometers and calls the show_miles function to convert it
def main():
    #Ask the user for the distance in kilometers
    kilometers = float(input("Distance in kilometers: "))
    
    #Display the distance converted to miles
    show_miles(kilometers)

#The show_miles function converts the parameter km from kilometers to miles and displays it
def show_miles(km):
    #Calculate miles
    miles = km * conversionfactor

    #Display the miles
    print(km, "kilometers equals", miles, "miles")

#Call the main function, makes the function able to run
main()
