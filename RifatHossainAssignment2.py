'''
INF360 - Programming in Python

Assignment 2

I,  Rifat Hossain  , affirm that the work submitted for this assignment is entirely my own. I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism, or the use of unauthorized
materials. This includes, but is not limited to, the use of resources such as Chegg, MyCourseHero, StackOverflow, ChatGPT, or other AI assistants, except where explicitly permitted by the instructor. I have neither provided nor
received unauthorized assistance and have accurately cited all sources in adherence to academic standards. I understand that failing to comply with this integrity statement may result in consequences, including disciplinary actions
as determined by my course instructor and outlined in institutional policies. By signing this statement, I acknowledge my commitment to upholding the principles of academic integrity.

'''

# 1/1 point - Initial comments*
# 1/1 point - Use at least 2 different comparison operators.
# 1/1 point - Use at least 1 boolean operator (and, or, not).
# 2/2 points - Write at least 1 if statement that MUST contain 2 elif statements and 1 else statement.
# 2/2 points - Write at least 1 while statement that contains a break and continue.
# 2/2 points - Write at least 1 for loop using the range() method.
# 1/1 point - Use the import keyword to import the random module. Use the random.randint() function somewhere in your script.

import random
import sys

print("Welcome to the Greencity Hotel!")
print("")

while True:
    resYesNo=input("Would you like to proceed with reservation? (Y/N) ")
    print("")
    
    if resYesNo == 'Y' or resYesNo == 'y' :
        
        print("Great! Following Suites are available: ")
        print("")
        print("#" * 40)
        print("")
        roomTypes = ["1) Standard Room - 2 to 4 Guests", "2) Standard Suite - 2 to 4 Guests", "3) Premium Suite - 5 to 7 Guests", "4) Presidential Suite - 6 to 10 Guests"]
        
        for i in roomTypes:
            print(i)
        print("")
        print("#" * 40)
        print("")
        
        for i in range(1):
            myNumber = int(input("Massive Discount Opportunity Today! Please type a number between 1 to 4 to win a '20%' discount on this reservation: "))
            randomNumber = random.randint(1, 4)
            if randomNumber == myNumber:
                print("")
                print ("Contgratulations! You've won the 20% special discount today.")
            else:
                print("")
                print ("Sorry, no discount this time. Good luck next time.")
        print("")        
        print("Now let's start the reservation process....")
        print("")
        ageCheck = int(input("How old are you? "))
        if ageCheck > 18:
            print("Great! You're old enough to make a reservation. Just need few more details.")
            nameFirst = input("What's first name? ")
            nameLast = input("What's your last name? ")
            numGuest = input("How many guests will you have? ")
            # Checks to see if the input of numGuest variable is empty.
            if numGuest == "":
                print("Invalid entry! Please start from the beginnig.")
                continue
            elif 2 <= int(numGuest) <= 4:
                print("You can reserve a 'Standard Room' Or 'Startdard Suites' for " + str(numGuest) + " guests.")
                print("")
                break
            elif 5 <= int(numGuest) <= 7:
                print("You can reserve a 'Premium Suite' for " + str(numGuest) + " guests.")
                print("")
                break
            elif 6 <= int(numGuest) <= 10:
                print("You can reserve a 'Presidential Suite' for " + str(numGuest) + " guests.")
                print("")
                break
            elif 10 < int(numGuest):
                print("You have to reserve mulptle suites for that many guests.")
                print("")
                break        
            else:
                print("Invalid entry! Please start from the beginnig.")
                print("")
        else:
            print("Sorry, you're not old enough to make a reservation.")
            print("")
            break
    elif resYesNo == 'N' or resYesNo == 'n':   
        print("No problem at all. Goodbye!")
        print("")
        sys.exit()  
    else:   
        print("You've provided an invalid input. Try again!")
        print("")

