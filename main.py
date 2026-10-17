#********************************************************************************
# Author:       Gabi Peña + Samantha Vialpando
# Assignment:   Lab 4
# Date:         10/16/2026
# Description:  This is a ticket and parking pre-sales webpage for the 
#               Oregon Zoo. It will ask the user how many tickets it needs, how
#               long it will be staying, and then print a final receipt. This pro-
#               gram also allows the user to add more tickets or time until it
#               decides to quit.
# Input:        user_choice, parking_time, ticker_number
# Output:       ticket_price, parking_price, final_total, ticket_tax
# Sources:      Lab 3 Assignment Instructions & Murach's Python Programming
#********************************************************************************

import tickets as t
import parking as p

def main():
    # define vars
    final_total, final_ticket_price, final_ticket_price, total_tickets= 0, 0, 0, 0
    total_hours_parked, final_parking_total = 0, 0
    # welcome message from the zoo
    # menu displays tickets, parking, and quit
    welcome_message()
    display_menu() 

    user_choice = get_input("Enter input (t/p/q): ")
    if user_choice != "q":
        while user_choice != "q":
            if (user_choice == "t"):
                # call ticket module functions
                ticket_price, ticket_number = t.ticketCalculations()
                ticket_tax = t.taxCalculations(ticket_price)
                new_ticket_price = t.totalCalculations(ticket_price, ticket_tax)
                # get final total of tickets and total tickets sold
                final_ticket_price += new_ticket_price
                total_tickets += ticket_number
            else:
                # gettting parking time and saves parking price
                parking_time = p.get_parking_time("Enter number of parking hours: ")
                parking_price = p.get_parking_cost(parking_time, 3) # parking cost set to $3
                # save total hours parked and total price 
                total_hours_parked += parking_time
                final_parking_total += parking_price
            #display user choice again to repeat or break the loop
            display_menu()
            user_choice = get_input("Enter T or P, or input Q to quit: ")
        #get final cost of both tickets and parking
        final_total += final_parking_total + final_ticket_price
        # display final receipt
        display_receipt(total_tickets, final_ticket_price, total_hours_parked, 
                    final_parking_total, final_total)
        # display goodbye message
        goodbye_message()
    else:
        #display goodbye message anyway if user chooses to quit immediately
        goodbye_message()

def welcome_message():
    print("Welcome to the Oregon Zoo ticket and parking store")

def display_menu():
    print("\nMenu")
    print("T - Ticket menu")
    print("P - Parking menu")
    print("Q - Quit")

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

def display_receipt(total_tickets, final_ticket_price, total_hours_parked, 
                    final_parking_total, final_total):
    print("\n            Basket total")
    print("{: <20}{: >10}".format("Tickets purchased:", total_tickets))
    print("{: <20}{: >10}".format("Tickets subtotal:", "$"+final_ticket_price))
    print("{: <20}{: >10}".format("Hours parked:", total_hours_parked))
    print("{: <20}{: >10}".format("Parking subtotal:", "$"+final_parking_total))
    print("{: <20}{: >10}".format("Final cost:", "$"+final_total))

def goodbye_message():
    print("\nThank you for visiting the Oregon Zoo!")

main()
