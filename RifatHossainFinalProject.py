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

# Setup logging
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
logging.debug('Start of program')

# Try importing data module which contains room information
try:
    from data import *
    logging.debug("data.py file loaded successfully")
except:
    print("My data.py is missing! Program will exit now.")
    logging.critical("data.py is missing! Investigate!")
    sys.exit()

# Hotel logo as a banner
hotelLogo = r"""                                                             
 _____ _             ____                          _ _           _   _       _       _ 
|_   _| |__   ___   / ___|_ __ ___  ___ _ __   ___(_) |_ _   _  | | | | ___ | |_ ___| |
  | | | '_ \ / _ \ | |  _| '__/ _ \/ _ \ '_ \ / __| | __| | | | | |_| |/ _ \| __/ _ \ |
  | | | | | |  __/ | |_| | | |  __/  __/ | | | (__| | |_| |_| | |  _  | (_) | ||  __/ |
  |_| |_| |_|\___|  \____|_|  \___|\___|_| |_|\___|_|\__|\__, | |_| |_|\___/ \__\___|_|
                                                         |___/                                                                                                                                    
"""

# Reservation class to store individual reservation data
class Reservation:
    def __init__(self, name, email, guests, room, cost):
        self.res_id = f"GREENCITY{random.randint(1000, 9999)}"
        self.name = name
        self.email = email
        self.guests = guests
        self.room = room
        self.cost = cost
        logging.info(f"Reservation created for {name} in room {room}, cost: ${cost}")

    def display_confirmation(self):
        logging.debug(f"Displaying confirmation for {self.res_id}")
        print("\nReservation Confirmed!")
        print(f"Reservation ID: {self.res_id}")
        print(f"Name: {self.name}\nEmail: {self.email}\nGuests: {self.guests}\nRoom: {self.room}\nTotal Cost: ${self.cost}")
        print("")
        print(f"An email has been sent to {self.email} with more details.")

# Hotel class to manage the hotel system
class Hotel:
    def __init__(self, rooms):
        self.rooms = rooms
        self.reservations = []
        logging.info("Hotel instance created with room data.")

    def show_available_rooms(self):
        logging.debug("Displaying available rooms")
        print('Available Suites'.center(65, '-'))
        print("")
        for name, detail in self.rooms.items():
            print(f"{name.ljust(20, ' ')} - ${detail['price']} per night ({detail['available']} available, {detail['min']}-{detail['max']} Guests)")
        print("-" * 65)

    def get_discount(self):
        try:
            print("")
            guess = int(input("Massive Discount Opportunity Today! Type a number between 1 to 4: "))
            if 1 <= guess <= 4:
                rand = random.randint(1, 4)
                if guess == rand:
                    logging.info("User won 20% discount.")
                    print("Congratulations! You've won a 20% discount.")
                    return 0.8
                else:
                    logging.info("User guessed wrong. No discount.")
                    print("Sorry, no discount this time. Good luck next time.")
            else:
                logging.warning("User input for discount was out of range.")
                print("Invalid input. No discount applied.")
        except ValueError:
            logging.warning("User input for discount was not a number.")
            print("Invalid input. No discount applied.")
        return 1.0

    def get_guest_info(self):
        while True:
            try:
                age = int(input("\nHow old are you? "))
                if age < 18:
                    logging.warning("Underage user tried to make a reservation.")
                    print("Sorry, you're not old enough to make a reservation.")
                    sys.exit()
                break
            except ValueError:
                logging.warning("Invalid age entered.")
                print("Invalid age. Please enter a number.")

        name_first = input("What's your first name? ").strip()
        name_last = input("What's your last name? ").strip()
        full_name = f"{name_first.title()} {name_last.title()}"

        while True:
            email = input("Enter your email: ").strip()
            email_regex = re.compile(r"^[\w.-]+@[\w.-]+\.\w+$")
            if email_regex.search(email):
                break
            logging.warning("Invalid email format entered.")
            print("Invalid email format. Try again.")

        while True:
            try:
                guests = int(input("How many guests will you have? "))
                if guests <= 0:
                    logging.warning("Invalid number of guests entered.")
                    print("Number of guests must be greater than 0.")
                    continue
                return full_name, email, guests
            except ValueError:
                logging.warning("Non-numeric input for number of guests.")
                print("Please enter a valid number.")

    def select_room(self, num_guests):
        for room, info in self.rooms.items():
            if info['min'] <= num_guests <= info['max'] and info['available'] > 0:
                logging.info(f"Room '{room}' selected for {num_guests} guests")
                print(f"You can reserve a '{room}' for {num_guests} guests.")
                return room
        logging.error("Multiple suites needed since guests number is more than 10.")
        print("Please book multiple suites for guests more than 10.")
        sys.exit()

    def confirm_booking(self, name, email, guests, room, discount):
        self.rooms[room]['available'] -= 1
        cost = int(self.rooms[room]['price'] * discount)
        reservation = Reservation(name, email, guests, room, cost)
        self.reservations.append(reservation)
        logging.info(f"Booking confirmed for {name}, Room: {room}, Cost: ${cost}")
        reservation.display_confirmation()

# Main function to run the program
def main():
    print(hotelLogo)
    print("Welcome to the Greencity Hotel!")
    hotel = Hotel(rooms)

    while True:
        proceed = input("\nWould you like to proceed with a reservation? (Y/N): ").strip().lower()
        print("")
        if proceed == 'n':
            logging.info("User chose not to proceed with reservation.")
            print("No problem at all. Goodbye!")
            sys.exit()
        elif proceed != 'y':
            logging.warning("Invalid input for proceeding with reservation.")
            print("Invalid input. Try again!")
            continue

        hotel.show_available_rooms()
        discount = hotel.get_discount()
        print("\nLet's start the reservation process...")
        name, email, guests = hotel.get_guest_info()
        room = hotel.select_room(guests)
        hotel.confirm_booking(name, email, guests, room, discount)

        again = input("\nWould you like to make another reservation? (Y/N): ").strip().lower()
        if again != 'y':
            logging.info("User ended session after one or more reservations.")
            print("Thank you for using the Greencity Hotel Reservation System. Goodbye!")
            break

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.critical(f"Unhandled exception occurred: {e}")
    finally:
        logging.debug('End of program')
