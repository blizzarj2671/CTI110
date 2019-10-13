#CTI-110
#P4HW1 - Expenses
#Jacob Blizzard
#Sep 18, 2019
#

##Prompt the user to enter a monetary value such as their bank account
##Prompt the user to enter a name and amount for an expense
##The program will subtract the expense from the original value and keep track of names
##The program will also keep track of the total cost of all the expenses and how much money in the account is left
##Record everything with reciept like prints and make them for each expense

#Disclaimer as to not confuse people and make it noticable
print("//-------------------------------------------------------------------------//")
print("Expense Calculator: Please do not put in any commas when using monetary value")
print("//-------------------------------------------------------------------------//")
print(" ")
print("//-------------------------------------------------------------------------//")
#Make the account amount input
print("What is the monetary ammount in the withdrawal acount?: ")
originalamount = float(input("$ "))

#Make a variable for the expense number
expensenum = 1

#Make a variable to the while loop
whileloop = 1

#Make the Total Cost variable
Total = 0

#Make the while loop
while whileloop == 1:
    
    #Ask the user for the name of the expense
    print("What is the name of expense", expensenum, ": ")
    expensename = input()
    
    #Ask the user for the amount of the expense
    print("What is the amount spent for", expensename, ": ")
    expenseamount = float(input("$ "))

    #Make a variable for the second loop
    whileloop2 = 1
    
    #Determine if yes or no or other
    while whileloop2 == 1:
        
        #Ask whether the user would like to add another expense
        print("Would you like to add another expense?:")
        decision = input()
        
        #What to do if it is yes, Yes, or y
        if decision == "yes" or decision == "Yes" or decision == "y":
            
            #Add to the Total variable for the total cost
            Total = Total + expenseamount

            #Make a variable for how much money is left in the account
            afteramount = originalamount - Total
            
            #Make reciept for the expense
            print(" ")
            print("Amount in account before expense", expensenum) #Show the original amount
            print(format(originalamount, ",.2f"))
            print("//--------------------------//")
            print("      Expense Calculator      ")  
            print("------------------------------")    
            print("Expense                 Amount")      
            print("==============================")        
            print(expensename,"                 $", format(expenseamount, ",.2f")) #Show the expense's information
            print("//--------------------------//")
            print("Amount in account after expense", expensenum) #Show the balance left in the account
            print("$", format(afteramount, ",.2f"))
            print(" ")

            #Print the total variable and format it to let the user know
            print("Total so far: $", format(Total, ",.2f"))
            print(" ")

            #Add one to the expensenum variable so it shows up as "2"
            expensenum = expensenum + 1

            #Make the second loop end
            whileloop2 = whileloop2 - 1
            
        #End the calculations and make a receipt if no, No, or n
        elif decision == "no" or decision == "No" or decision == "n":

            if expensenum == 1:
                Total = expenseamount
                afteramount = originalamount - Total

            else:
                Total = Total + expenseamount
                afteramount = originalamount - Total

            #Show receipt for final expense
            print(" ")
            print("Amount in account before expense", expensenum) #Show the original amount
            print(format(originalamount, ",.2f"))
            print("//--------------------------//")
            print("      Expense Calculator      ")  
            print("------------------------------")    
            print("Expense                 Amount")      
            print("==============================")        
            print(expensename,"                 $", format(expenseamount, ",.2f")) #Show the final expense's information
            print("//--------------------------//")
            print("Amount in account after expense", expensenum) #Show the final balance left in the account
            print("$", format(afteramount, ",.2f"))
            print(" ")
            print("Total amount of expenses:", expensenum) #Show the total amount of expenses used
            print("Total amount spent:$ ", format(Total, ",.2f")) #Show the total amount of money in the expenses

            #Make the second loop end
            whileloop2 = whileloop2 - 1
            
            #Get rid of the variable which makes the loop run
            whileloop = whileloop - 1

            
        #Make an error if yes or no is not inputed and restate the question
        else:
            print(" ")
            print("Error: You did not type in yes or no")
            print(" ")

#DONT MAKE RECIEPT AT END - IT WILL NOT WORK
