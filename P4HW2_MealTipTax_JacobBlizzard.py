#CTI-110
#P4HW2 - MealTipTax
#Jacob Blizzard
#Sep 23, 2019
#

##The user will input the meal amount and tax for it
##The program will calculate with 16, 18, or 20 percent tax and will prompt the user for a correct tip before moving on
##The program will show the calculated meal and tax and stuff
##The program will prompt the user if they want to redo their reciept, it will terminate if no

#Welcome the user
print("//-----------------------------------------//")
print("Welcome to the meal calculator")
print("//-----------------------------------------//")

#Ask the user to enter the charge for food
FoodCharge = float(input("Enter the meal's charge: "))

###Create error messages if the tip is not correct, make a default percent
###Old code
##if TipAmount == .16:
##    TipAmount = .16
##elif TipAmount == .18:
##    TipAmount = .18
##elif TipAmount == .20:
##    TipAmount = .20
##else:
##    print("Error: Tip is not 16%, 18%, or 20%")
##    TipAmount = .18
##    print("A default of 18% was used")

#Make a variable for the loop that controls the entire program
whileloop2 = 1

#Make a variable so the code works
qbt = "yes"

#Make the loop
while whileloop2 == 1:
    if qbt == "No" or qbt == "no" or qbt == "n":
        whileloop2 = 0
        whileloop = 0
        print("Thank you for using this calculator")
    elif qbt == "Yes" or qbt == "yes" or qbt == "y":

        #New code for the error messages if the tip is not correct, make a variable for the loop
        whileloop = 1

        #Make a loop for the tax
        while whileloop == 1:
            #Ask the user to enter the tip for the server, make sure they put the correct tip in
            print("Enter the tip percentage for the server")
            print("Please put in a decimal format (18% = .18)")
            TipAmount = float(input("16%, 18%, 20% Recommended: "))
            if TipAmount == .16:
                TipAmount = .16
                whileloop = 0
            elif TipAmount == .18:
                TipAmount = .18
                whileloop = 0
            elif TipAmount == .20:
                TipAmount = .20
                whileloop = 0
            else:
                print(" ")
                print("Error: Tip is not 16%, 18%, or 20%")
                print(" ")
                whileloop = 1

        #The Right Tip Amounts, Asking for the state tax
        StateTax = .06

        #Calculate tip
        CalcTip = FoodCharge * TipAmount

        #Calculate tax
        CalcTax = FoodCharge * StateTax

        #Calculate total cost
        TotalCost = FoodCharge + CalcTip + CalcTax

        #Display the meal amount
        print("Meal: $", format(FoodCharge, ",.2f"))

        #Display the tip
        print("Tip: $", format(CalcTip, ",.2f"))

        #Display the tax
        print("Tax: $", format(CalcTax, ",.2f"))

        #Display the total cost
        print("Total Cost: $", format(TotalCost, ",.2f"))

        #Make the whileloop 1 so the code works
        whileloop = 1

        #Determine if the variables are right to prompt the user for another tip
        if whileloop == 1:
            qbt = input("Would you like to input a different tip: ")#question before termination
            whileloop2 = 1
        else:
            print("Thank you for using this code")

        
