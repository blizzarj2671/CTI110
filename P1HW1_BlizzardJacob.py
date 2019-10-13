# This program calculates gross pay.

def main():
    # Get the number of hours worked.
    hours = int(input("How many hours did you work?"))

    # Get the hourly pay rate.
    pay_rate = float(input("Enter your hourly pay rate:"))

    #Calculate the gross pay.
    gross_pay = hours + pay_rate

    #Display the gross pay.
    print("Gross pay: $", format(gross_pay, ",.2f"), sep="")

#Call the main function.
main()


# This program demonstrates how the range
# function can be used with a for loop.

def main():
    # Print a message five times.
    for x in range(5):
        print ("This is your gross pay, also its Jacob Blizzard.")

# Call the main function.
main()
