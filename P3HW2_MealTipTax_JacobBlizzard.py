#CTI-110
#P3HW2 - MealTipTax
#Jacob Blizzard
#Sep 11, 2019
#

#Ask the user to enter the charge for food
FoodCharge = float(input("Enter the meal's charge: "))

#Ask the user to enter the tip for the server, make sure they put the correct tip in
print("Enter the tip percentage for the server")
TipAmount = float(input("16%, 18%, 20% Recommended: "))

#Create error messages if the tip is not correct, make a default percent
if TipAmount == .16:
    TipAmount = .16
elif TipAmount == .18:
    TipAmount = .18
elif TipAmount == .20:
    TipAmount = .20
else:
    print("Error: Tip is not 16%, 18%, or 20%")
    TipAmount = .18
    print("A default of 18% was used")

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
