#********************************************************************************
# Author:       Gabi Peña + Samantha Vialpando
# Assignment:   Lab 3
# Date:         10/16/2026
# Description:  This is a ticket and parking pre-sales webpage for the 
#               Oregon Zoo. It will ask the user how many tickets it needs, how
#               long it will be staying, and then print a final receipt. This pro-
#               gram also allows the user to add more tickets or time until it
#               decides to quit.
# Input:        user_choice, parking_time, ticker_number
# Output:       ticket_price, parking_price, final_total
# Sources:      Lab 3 Assignment Instructions & Murach's Python Programming
#********************************************************************************

#import Gabis module
import parking as p
import tickets as t

def main():
    final_total = 0
    welcome_message()
    display_menu() 

    user_choice = get_input("enter input (t/p/q): ")
    if user_choice != "q":
        while user_choice != "q":
            if (user_choice == "t"):
                print("delete me") #placeholder function so the
                #else block stops yelling at me.
                #get ticket_number (module function)
                #get ticket_price (module function)
                #add ticket_price to final_total
            else:
                parking_time = p.get_parking_time("Enter number of parking hours: ")
                parking_price = p.get_parking_cost(parking_time, 3)
                final_total += parking_price
            user_choice = get_input("Enter T or P, or input Q to quit: ")
        
        display_reciept()
        goodbye_message()
    else:
        goodbye_message()

def welcome_message():
    print("Welcome to the Oregon Zoo ticket and parking store")

def display_menu():
    print("\nMenu")
    print("T - Ticket menu")
    print("P - parking menu")
    print("Q - quit")

def get_input(prompt):
    success = False
    while not success:
        try:
            choice = input(prompt)
            success = True
        except:
            print("Invalid input. Try again")
        choice.lower()
        choice.strip()
    return choice[0]

def display_reciept():
    '''
    finish this later. 
    probably using some formating
    so it looks nice
    '''

def goodbye_message():
    '''
    finish this later. probably a one line message
    '''


