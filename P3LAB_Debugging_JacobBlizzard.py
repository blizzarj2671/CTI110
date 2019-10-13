#CTI-110
#P3LAB - Debugging
#Jacob Blizzard
#Sep 11, 2019
#

#Ask for score
score = int(input("Input the score: "))

#Score Variables
A_score = 90
B_score = 80
C_score = 70
D_score = 60
F_score = 50

#Come up with the grades
if score > 100:
    print("Error: Score cannot be higher than 100")
elif score < 0:
    print("Error: Score cannot be lower than 0")
elif score >= A_score:
    print("Your grade is an A.")
elif score >= B_score:
    print("Your grade is a B.")
elif score >= C_score:
    print("Your grade is a C.")
elif score >= D_score:
    print("Your grade is a D.")
else:
    print("Your grade is a F.")

