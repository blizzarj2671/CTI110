#Make a menu driven program that gives simple math quizzes with two random numbers to be added
#Sep 30, 2019
#CTI-110 P5HW1 - Math Quiz
#Jacob Blizzard
#

#For exercise #11:
#import random
#get a random integer
#make user type in an answer
#determine if answer is right or wrong
#display the determination

#For the menu:
#make a main menu that consists of taking the math quiz or exiting the program
#make the user input what they want to do
#do whatever the user inputs

#Import random
import random

#Welcome the user
print("//Welcome to the Python Math Quiz")
print("//Created by: Jacob Blizzard")
print(" ")

#Make the main function of the system
def main():

    #Make a loop in case the user inputs a wrong decision for the menu
    middeci = 0
    errorloop = 1
    while errorloop == 1 or middeci == 2:

        #Make the menu layout
        middeci = 0
        print("//Main Menu")
        print("//------------------------//")
        print("//1- Add Random Numbers")
        print("//2- Subtract Random Numbers")
        print("//3- Exit")
        print(" ")
        decinput = int(input("What would you like to do?: "))

        #Start the addition game if the user inputs 1
        if decinput == 1:
            print(" ")
            print("//Starting addition game...")
            print(" ")
            print("//You have two numbers to try and find the solution")
            print("//You have two chances, good luck")
            print(" ")

            #Make the variable and loop for the addition guessing game
            addition = 1
            while addition == 1 or middeci == 1:
                #Make the numbers appear and determine the solution
                for count in range(1):
                    num1 = random.randint(-627, 627)
                    num2 = random.randint(-627, 627)
                    solution = num1 + num2
                    
                    #Instead of guessing, here's the numbers to test the code
                    #//
                    #Only enable for debugging purposes \/
                    print(" ")
                    print("//DEBUGGING PURPOSES//")
                    print(solution)
                    print("//DEBUGGING PURPOSES//")
                    print(" ")
                    #Only enable for debugging purposes /\
                    #//

                    #Print the numbers and make the user input the answer
                    print("//ADD//Here are your numbers...")
                    print(num1)
                    print(num2)
                    print(" ")
                    
                    #Make a variable for the guesses and addition whileloop
                    addwhile = 1
                    guesses = 0

                    #Start the loop
                    while addwhile == 1:
                        guess = int(input("What is the solution?: "))
                        
                        #Make the loop for three guesses
                        if guesses == 2 and guess != solution:
                            print(" ")
                            print("//Sorry, you have used up your two guesses")
                            print(" ")
                            addition = 0
                            addwhile = 0
                        
                        #If the number is too high
                        elif guess > solution and guesses != 2:
                            print(" ")
                            print("//Too high, try again")
                            print("//You have one more chance for this problem")
                            print(" ")
                            guesses = guesses + 1

                        #If the number is too low
                        elif guess < solution and guesses != 2:
                            print(" ")
                            print("Too low, try again")
                            print("//You have one more chance for this problem")
                            print(" ")
                            guesses = guesses + 1

                        #Otherwise they are right
                        elif guess == solution:
                            print(" ")
                            print("//Congrats, you have the right answer")
                            print(" ")
                            addwhile = 0

                        #Make an error message for else
                        else:
                            print("//The program had an unexpected error and needs to restart")
                            addwhile = 0

                    #Make a continuation message
                    addwhile = 0
                    addition = 0
                    errorloop = 1
                    print("//1- Continue")
                    print("//2- Main Menu")
                    middeci = int(input("Would you like to continue? "))
                    print(" ")
                    
        #Start the subtraction game if the user inputs 2
        elif decinput == 2:
            print(" ")
            print("//Starting subtraction game...")
            print(" ")
            print("//You have two numbers to try and find the solution")
            print("//You have two chances, good luck")
            print(" ")

            #Make the variable and loop for the addition guessing game
            subtraction = 1
            while subtraction == 1 or middeci == 1:
                #Make the numbers appear and determine the solution
                for count in range(1):
                    num1 = random.randint(-627, 627)
                    num2 = random.randint(-627, 627)
                    solution = num1 - num2

                    #Instead of guessing, here's the numbers to test the code
                    #//
                    #Only enable for debugging purposes \/
                    print(" ")
                    print("//DEBUGGING PURPOSES//")
                    print(solution)
                    print("//DEBUGGING PURPOSES//")
                    print(" ")
                    #Only enable for debugging purposes /\
                    #//

                    #Print the numbers and make the user input the answer
                    print("SUB//Here are your numbers...")
                    print(num1)
                    print(num2)
                    print(" ")

                    #Make a variable for the guesses and addition whileloop
                    subwhile = 1
                    guesses = 0

                    while subwhile == 1:
                        guess = int(input("What is the solution?: "))
                        
                        #Make the loop for three guesses
                        if guesses == 2 and guess != solution:
                            print(" ")
                            print("//Sorry, you have used up your two guesses")
                            print(" ")
                            subtraction = 0
                            subwhile = 0
                        
                        #If the number is too high
                        elif guess > solution and guesses != 2:
                            print(" ")
                            print("//Too high, try again")
                            print("//You have one more chance for this problem")
                            print(" ")
                            guesses = guesses + 1

                        #If the number is too low
                        elif guess < solution and guesses != 2:
                            print(" ")
                            print("Too low, try again")
                            print("//You have one more chance for this problem")
                            print(" ")
                            guesses = guesses + 1

                        #Otherwise they are right
                        elif guess == solution:
                            print(" ")
                            print("//Congrats, you have the right answer")
                            print(" ")
                            subwhile = 0

                        #Make an error message for else
                        else:
                            print("//The program had an unexpected error and needs to restart")
                            subwhile = 0

                    #Make a continuation message
                    subwhile = 0
                    subtraction = 0
                    errorloop = 1
                    print("//1- Continue")
                    print("//2- Main Menu")
                    middeci = int(input("Would you like to continue? "))
                    print(" ")

        #Exit the program if the user inputs 3
        elif decinput == 3:
            errorloop = 0
            meddeci = 0
            print(" ")
            print("//Exiting program...")

        #Make an error loop
        else:
            print(" ")
            print("/Error: No option was decided")
            print(" ")
            errorloop = 1
            
#Call the main function so it'll work
main()
