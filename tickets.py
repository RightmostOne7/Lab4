# ticket_module.py
TAX_RATE = 0.07


def ticketCalculations():
    ticketPrice = 25
    ticketSubtotal = 0
# ticket purchase calculation loop
    while True:
        try:
            # user input loop & validation
            ticketPurchase = int(input("How many tickets would you like to purchase? "))
            if ticketPurchase > 0:
                ticketSubtotal += ticketPrice * ticketPurchase
                print(f"Your current subtotal is ${ticketSubtotal:.2f}")
                # user input loop & validation
                repeatTicketInput = input("Would you like to add another ticket? (y/n) ").lower().strip()
                while repeatTicketInput != "y" and repeatTicketInput != "n":
                    print("Invalid input, please type y or n.")
                    repeatTicketInput = input("Would you like to add another ticket? (y/n) ").lower().strip()

                if repeatTicketInput == "n":
                    break
            else:
                print("Please enter a number greater than 0.")
        except:
            print("Invalid input, please enter a whole number.")
    return ticketSubtotal


def taxCalculations(ticketSubtotal):
    taxAmount = ticketSubtotal * TAX_RATE
    return taxAmount


def totalCalculations(ticketSubtotal, taxAmount):
    total = ticketSubtotal + taxAmount
    return total


def printReceipt(ticketSubtotal, taxAmount, total):
    print("\n--- Receipt ---")
    print(f"Subtotal: ${ticketSubtotal:.2f}")
    print(f"Tax: ${taxAmount:.2f}")
    print(f"Ticket Total: ${total:.2f}")


# module testing
# def main():
#     subtotal = ticketCalculations()
#     tax = taxCalculations(subtotal)
#     total = totalCalculations(subtotal,tax)
#     printReciept(subtotal, tax, total)
#
# if __name__ == "__main__":
#  main()




