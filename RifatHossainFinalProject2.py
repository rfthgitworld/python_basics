'''
INF360 - Programming in Python

Final Project

I,  Rifat Hossain  , affirm that the work submitted for this assignment is entirely my own. I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism, or the use of unauthorized
materials. This includes, but is not limited to, the use of resources such as Chegg, MyCourseHero, StackOverflow, ChatGPT, or other AI assistants, except where explicitly permitted by the instructor. I have neither provided nor
received unauthorized assistance and have accurately cited all sources in adherence to academic standards. I understand that failing to comply with this integrity statement may result in consequences, including disciplinary actions
as determined by my course instructor and outlined in institutional policies. By signing this statement, I acknowledge my commitment to upholding the principles of academic integrity.

'''

# ----------------------------------------------------------------------------------------
# Greencity Hotel Reservation System
# ----------------------------------------------------------------------------------------
# This Python program simulates a hotel reservation system for Greencity Hotel.
# It allows users to:
#   - View available rooms with guest capacity and pricing.
#   - Participate in a number-guessing game to win a discount.
#   - Enter personal information with input validation including email and age.
#   - Ensures the user making the reservating is an adult (Over 18 year of age).
#   - Select an appropriate room based on number of guests.
#   - Confirm the reservation with a unique reservation ID and cost summary.
#   - Loop to allow multiple reservations.
# ------------------------------------------------------------------------------------------

import re
import random
import sys
import logging 

logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')


logging.debug('Start of program')

try:
    from data import *  
    logging.debug("data.py file loaded successfully")
except:
    print("My data.py file is missing! Program will exist now.")
    logging.critical("data.py is missing! Investigate!")
    sys.exit()


hotelLogo = r"""                                                           
 _____ _             ____                          _ _           _   _       _       _ 
|_   _| |__   ___   / ___|_ __ ___  ___ _ __   ___(_) |_ _   _  | | | | ___ | |_ ___| |
  | | | '_ \ / _ \ | |  _| '__/ _ \/ _ \ '_ \ / __| | __| | | | | |_| |/ _ \| __/ _ \ |
  | | | | | |  __/ | |_| | | |  __/  __/ | | | (__| | |_| |_| | |  _  | (_) | ||  __/ |
  |_| |_| |_|\___|  \____|_|  \___|\___|_| |_|\___|_|\__|\__, | |_| |_|\___/ \__\___|_|
                                                         |___/                                                                                                                                      

"""

reservations = []

# A function that displays all available rooms and their details.
def show_available_rooms():
    logging.info("Displaying available rooms.")
    print('Available Suites'.center(65, '-'))
    print("")  
    for name, detail in rooms.items():
        print(f"{name.ljust(20, ' ')} - ${detail['price']} per night ({detail['available']} available, {detail['min']}-{detail['max']} Guests)")
    print("-" * 65)

# Offers a discount if user guesses a random number correctly.
def get_discount():
    try:
        print("")
        guess = int(input("Massive Discount Opportunity Today! Type a number between 1 to 4: "))
        logging.debug(f"User guessed: {guess}")
        if 1 <= guess <= 4:
            rand = random.randint(1, 4)
            if guess == rand:
                logging.info("User won a discount.")
                print("Congratulations! You've won a 20% discount.")
                return 0.8  # Apply 20% discount.
            else:
                logging.info("User did not win the discount.")
                print("Sorry, no discount this time. Good luck next time.")
        else:
            logging.warning("User guessed a number out of range.")
            print("Invalid input. No discount applied.")
    except ValueError as e:
        logging.error(f"Non-numeric input for discount guessing. Error: {e}")
        print("Invalid input. No discount applied.")
    return 1.0  # Full price if no discount.

# Gathers guest's name, email, age, and number of guests.
def get_guest_info():
    while True:
        try:
            age = int(input("\nHow old are you? "))
            logging.debug(f"Guest age input: {age}")
            if age < 18:
                logging.warning("Guest is underage.")
                print("Sorry, you're not old enough to make a reservation.")
                sys.exit()
            break
        except ValueError as e:
            logging.error(f"Invalid age input. Error: {e}")
            print("Invalid age. Please enter a number.")

    name_first = input("What's your first name? ").strip()
    name_last = input("What's your last name? ").strip()
    full_name = f"{name_first.title()} {name_last.title()}"
    logging.debug(f"Full name: {full_name}")

    while True:
        email = input("Enter your email: ").strip()
        email_regex = re.compile(r"^[\w.-]+@[\w.-]+\.\w+$")
        if email_regex.search(email):
            logging.debug(f"Email accepted: {email}")
            break
        logging.warning("Invalid email format.")
        print("Invalid email format. Try again.")

    while True:
        try:
            guests = int(input("How many guests will you have? "))
            logging.debug(f"Number of guests input: {guests}")
            if guests <= 0:
                logging.warning("Guests count must be greater than 0.")
                print("Number of guests must be greater than 0.")
                continue
            return full_name, email, guests
        except ValueError as e:
            logging.error(f"Invalid number of guests input. Error: {e}")
            print("Please enter a valid number.")

# Chooses a room based on number of guests and availability.
def select_room(num_guests):
    for room, info in rooms.items():
        if info['min'] <= num_guests <= info['max'] and info['available'] > 0:
            logging.info(f"Room selected: {room} for {num_guests} guests.")
            print(f"You can reserve a '{room}' for {num_guests} guests.")
            return room
    logging.error("Multiple suites needed since guests number is more than 10.")
    print("Please book multiple suites for guests more than 10.")
    sys.exit()

# Confirms and saves the booking, then displays reservation details.
def confirm_booking(name, email, guests, room, discount):
    rooms[room]['available'] -= 1  # Decrease room availability.
    res_id = f"GREENCITY{random.randint(1000, 9999)}"  # Generate random reservation ID.
    cost = int(rooms[room]['price'] * discount)  # Calculate final price with discount.
    reservation = {
        'ID': res_id,
        'Name': name,
        'Email': email,
        'Guests': guests,
        'Room': room,
        'Cost': cost
    }
    reservations.append(reservation)  # Save reservation to the list.
    logging.info(f"Reservation created: {reservation}")
    print("\nReservation Confirmed!")
    print(f"Reservation ID: {res_id}")
    print(f"Name: {name}\nEmail: {email}\nGuests: {guests}\nRoom: {room}\nTotal Cost: ${cost}")
    print("")
    print(f"An email has been sent to {email} with more details.")

# Main driver function to run the hotel reservation process.
def main():
    print(hotelLogo)
    print("Welcome to the Greencity Hotel!")
    logging.info("Program started successfully.")

    while True:
        proceed = input("\nWould you like to proceed with a reservation? (Y/N): ").strip().lower()
        print("")
        if proceed == 'n':
            print("No problem at all. Goodbye!")
            sys.exit()
        elif proceed != 'y':
            logging.warning("Invalid input for reservation confirmation.")
            print("Invalid input. Try again!")
            continue

        show_available_rooms()
        discount = get_discount()
        print("\nLet's start the reservation process...")
        name, email, guests = get_guest_info()
        room = select_room(guests)
        confirm_booking(name, email, guests, room, discount)

        again = input("\nWould you like to make another reservation? (Y/N): ").strip().lower()
        if again != 'y':
            logging.info("User ended the reservation session.")
            print("Thank you for using the Greencity Hotel Reservation System. Goodbye!")
            break

# Run the program...

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.critical(f"Unhandled exception occurred: {e}")
    finally:
        logging.debug('End of program')
