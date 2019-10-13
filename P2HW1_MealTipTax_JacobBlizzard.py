#Create a program that calculates the total amount of a meal from a resturant
#September 4, 2019
#CTI-110 P2HW1 - Meal Tip Tax Calulator
#Jacob Blizzard
#

#Ask the user to enter the charge for food
FoodCharge = float(input("Enter the meal's charge: "))

#Ask the user to enter the tip for the server
TipAmount = float(input("Enter the tip percentage (in decimal form) for the server: "))

#Ask the user to enter the state tax
StateTax = float(input("Enter the state tax (in decimal form): "))

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
