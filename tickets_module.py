# ticket_module.py
def ticketCalculations():
    ticketPrice = 25
    ticketSubtotal = 0

    while True:
        try:
            ticketPurchase = int(input("How many tickets would you like to purchase? "))

            if ticketPurchase > 0:
                ticketSubtotal += ticketPrice * ticketPurchase
                print(f"Your current subtotal is ${ticketSubtotal}")


                repeatTicketInput = input("Would you like to add another ticket? (y/n) ").lower()
                if repeatTicketInput != "y":
                    break

            else:
                print("Please enter a number greater than 0")


        except:
            print("Invalid input, please type a whole number.")

    return ticketSubtotal

def taxCalculations(ticketSubtotal):
    TAX_RATE = 0.07
    taxAmount = ticketSubtotal * TAX_RATE
    return taxAmount

def totalCalculations(ticketSubtotal, taxAmount):
    total = ticketSubtotal + taxAmount
    return total

def printReciept(ticketSubtotal, taxAmount, total):
    print("\n--- Recipept ---")
    print(f"Subtotal: ${ticketSubtotal}")
    print(f"Tax: ${taxAmount:.2f}")
    print(f"Total: ${total:.2f}")

# def main():
#     subtotal = ticketCalculations()
#     tax = taxCalculations(subtotal)
#     total = totalCalculations(subtotal,tax)
#     printReciept(subtotal, tax, total)
#
# if __name__ == "__main__":
#  main()




