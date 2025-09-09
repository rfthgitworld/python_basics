'''
INF360 - Programming in Python

Assignment 1

I,  Rifat Hossain  , affirm that the work submitted for this assignment is entirely my own. I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism, or the use of unauthorized
materials. This includes, but is not limited to, the use of resources such as Chegg, MyCourseHero, StackOverflow, ChatGPT, or other AI assistants, except where explicitly permitted by the instructor. I have neither provided nor
received unauthorized assistance and have accurately cited all sources in adherence to academic standards. I understand that failing to comply with this integrity statement may result in consequences, including disciplinary actions
as determined by my course instructor and outlined in institutional policies. By signing this statement, I acknowledge my commitment to upholding the principles of academic integrity.

'''

# 1/1 point - Initial comments*
# 2/2 points - Use of the print() function to display a welcome and prompt a question to the user.
# 2/2 points - Use of the input() function and store in a variable called myInput.
# 1/1 point - Use the print() function to print the contents of myInput.
# 2/2 points - Use two different math operators from Table 1-1 in your script. This may be used to manipulate some input from the user.
# 2/2 points - Use string concatenation.


myInput = input ('Welcome to Greencity Resort! Provide your first and last name to start a reservation: ')
print ('Hi, ' + myInput +'!' + ' We just need few more details for your reservation.')

age = input('How old are you? ')
print ('Thanks! You are ' + age + ' years old and you are old enough to reserve.')

# Number of days a visitor will be staying in the resort
duration = input('How many days will you be staying here? ')
print("")
print ('Contraguaitons! You will receive a 15% percent discount today as a first-time guest.')

# Regular price per night
regPrice = int(80)
discountRate = float(0.15)
# Discount calculations
savingTotal = int(duration) * regPrice * discountRate
# Total payment calculaitons
totalPayment = int(duration) * regPrice - savingTotal

print("")
print('Your total payment for ' + duration + ' day(s) will be: ' + '$' + str(totalPayment))
print('You are also receiving a discount of ' + '$'+ str(savingTotal))
print("")
print('Enjoy your stay at Greencity resort!')
print("")