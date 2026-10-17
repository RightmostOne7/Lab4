#********************************************************************************
# Author:       Gabi Peña + Samantha Vialpando
# Assignment:   Lab 4
# Date:         10/16/2026
# Description:  This is a ticket and parking pre-sales webpage for the 
#               Oregon Zoo. It will ask the user how many tickets it needs, how
#               long it will be staying, and then print a final receipt.
#               This program also allows the user to add more tickets or time until
#               it decides to quit.
#               Gabi - Ticket Module + Main
#               Samantha - Parking Module + Main
# Input:        userChoice, ticketPurchase, hoursParked, repeatTicketInput, repeatParkingInput
# Output:       ticketSubtotal, parkingSubtotal, finalSubtotal, finalTax, finalTotal
# Sources:      Lab 4 Assignment Instructions & Murach's Python Programming
#********************************************************************************
#import modules as variables
import parking as p
import tickets as t

# calling main functions
def main():
    welcomeMessage()
    runStoreLoop()
    goodbyeMessage()


# using input to make calculations
def runStoreLoop():
    finalSubtotal = 0
    finalTax = 0
    finalTotal = 0
    displayMenu()
    userChoice = getInput("Enter Input (t/p/q): ")

    while userChoice != "q":
        if userChoice == "t":
            ticketSubtotal = t.ticketCalculations()
            ticketTax = t.taxCalculations(ticketSubtotal)
            ticketTotal = t.totalCalculations(ticketSubtotal, ticketTax)
            t.printReceipt(ticketSubtotal, ticketTax, ticketTotal)

            # adding purchases together for grand total
            finalSubtotal += ticketSubtotal
            finalTax += ticketTax
        elif userChoice == "p":
            #calling parking module
            parkingSubtotal = p.parkingCalculations()
            parkingTax = p.taxCalculations(parkingSubtotal)
            parkingTotal = p.totalCalculations(parkingSubtotal, parkingTax)
            p.printReceipt(parkingSubtotal, parkingTax, parkingTotal)

            # adding purchases together for grand total
            finalSubtotal += parkingSubtotal
            finalTax += parkingTax
        else:
            print("Invalid input. Please enter 't', 'p', or 'q'.")

        displayMenu()
        userChoice = getInput("Enter Input (t/p/q): ")

    finalTotal = finalSubtotal + finalTax

# printing grand total (tickets + parking)
    print("\n===========================")
    print(f"Grand Subtotal: ${finalSubtotal:.2f}")
    print(f"Total Tax: ${finalTax:.2f}")
    print(f"Grand total: ${finalTotal:.2f}")
    print("===========================")


def welcomeMessage():
    print("Welcome to the Oregon Zoo ticket and parking store")


def displayMenu():
    print("\nMenu")
    print("T - Ticket menu")
    print("P - Parking menu")
    print("Q - Quit")


# gets user input
def getInput(prompt):
    success = False
    while not success:
        try:
            choice = input(prompt)
            success = True
        except:
            print("Invalid input. Try again")
    return choice.lower().strip()


def goodbyeMessage():
    print("Thank you for visiting the Portland Zoo and we hope you enjoyed your visit!")


if __name__ == "__main__":
    main()


