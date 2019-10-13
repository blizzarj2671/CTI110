#Write a function named feet_to_inches that accepts a number of feet as an argument
#Returns the number of inches in that many feet
#Sep 24, 2019
#CTI-110 P5T2_FeetToInches
#Jacob Blizzard
#

#The number of inches per feet
ipf = 12

#Main function
def main():
    #Get a number of feet from the user
    feet = int(input("Enter a number of feet: "))

    #Convert the feet into inches
    print(feet, "feet equals", feet_to_inches(feet), "inches")

#Use the feet_to_inches function to covert the feet
def feet_to_inches(feet):
    return feet * ipf

#Call the main function
main()
