#Make a program that generates a random number from 1 to 100 and ask the user to guess what the number is
#Sep 25, 2019
#CTI-110 P5HW1- Random Number
#Jacob Blizzard
#

#For exercise #20:
#import random
#get a random interger from 1 to 100
#make the user type in a guess
#determine whether it is higher, lower, or equal to the random number
#display the determination

#For the menu:
#make a main menu that consists of playing the game or exiting the program
#make the user input what they want to do
#do whatever the user inputs

#Import random
import random

#Welcome the user
print("//Welcome to python random number guessing game")
print(" ")

#Make the main function of the system
def main():
    
    #Make a loop incase the user inputs a wrong number for the menu
    errorloop = 1
    while errorloop == 1:
        print("//Main Menu")
        print("//---------------------------------//")
        print("//1- Play Random Number Guessing Game")
        print("//2- Exit the program")
        print(" ")
        decinput = int(input("What would you like to do?: "))

        #Start the game if the user inputs 1
        if decinput == 1:
            print(" ")
            print("//Starting game...")
            print(" ")
            print("//Try and guess a number between 1 to 100")
            print("//You have 6 guesses, good luck")
            print(" ")
            errorloop = 0

            #Make a variable for the main whileloop
            mainfunction = 1

            #Make a whileloop so the program can restart
            while mainfunction == 1:

                #Bring in the main function and it count only one number
                    for count in range(1):

                        #Make random introduce a random integer
                        number = random.randint(1, 100)

                        #Instead of guessing, here's the number to test the code
                        #//
                        #Only enable for debugging purposes \/
##                        print(" ")
##                        print("//DEBUGGING PURPOSES//")
##                        print(number)
##                        print("//DEBUGGING PURPOSES//")
##                        print(" ")
                        #Only enable for debugging purposes /\
                        #//

                        #Make a variable for the amount of guesses and the second whileloop
                        guesses = 0
                        whileloop = 1

                        #Make the whileloop a restart if the user gets the guess wrong
                        while whileloop == 1:

                            #Make the user type in a guess
                            print("//Next number...")
                            guess = int(input("Enter your guess from 1 to 100: "))

                            #Make the limit on guesses
                            if guesses == 6 and guess != number:
                                print(" ")
                                print("//Sorry, you have used up all of your guesses, try again with a new number")
                                print("//You had", guesses, "guesses for the number /", number, "/")
                                print(" ")
                                whileloop = 0

                            #If the number is too high and the amount of guesses so far
                            elif guess > number:
                                print(" ")
                                print("//Too high, try again")
                                print(" ")
                                guesses = guesses + 1
                                print("//You have", guesses, "guesses for this number")

                            #If the number is too low and the amount of guesses so far
                            elif guess < number:
                                print(" ")
                                print("//Too low, try again")
                                print(" ")
                                guesses = guesses + 1
                                print("//You have", guesses, "guesses for this number")
                                
                            #Otherwise they guessed correctly, display the amount of gusses for the number
                            elif guess == number:
                                print(" ")
                                print("//Congrats, you guessed correctly")
                                print(" ")
                                whileloop = 0
                                guesses = guesses + 1
                                print("//You had", guesses, "guesses for the number /", number, "/")

                            #Make an error message to fill in the else
                            else:
                                print("The program has had an unexpected error and needs to restart")
                                whileloop = 0
                                mainfunction = 1
                                
        #Make the program terminate if 2 is chosen
        elif decinput == 2:
            print(" ")
            print("//Exiting program...")
            errorloop = 0

        #Make an error if 1 or 2 is not chose
        else:
            print(" ")
            print("//Error: Neither option was inputed")
            print(" ")
            errorloop = 1
        
#Call the functions so it'll work
main()
