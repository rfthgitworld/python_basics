import random

# roomTypes = ["1) Standard Room - 2 to 4 Guests", "2) Standard Suite - 2 to 4 Guests", "3) Premium Suite - 5 to 7 Guests", "4) Presidential Suite - 6 to 10 Guests"]
# for i in roomTypes:
#     print(i)
     
for i in range(1):
    myNumber = int(input("Massive Discount Opportunity Today! Please type a number between 1 to 4 to win a '20%' discount on this reservation: "))
    randomNumber = random.randint(1, 4)
    if randomNumber == myNumber:
        print ("Contgratulations! You've won the 20% special discout today. ")
    else:
        print ("Sorry, no discount this time. Good luck next time.")

