# parking module
TAX_RATE = 0.07


def parkingCalculations():
    hourlyRate = 5.00
    parkingSubtotal = 0

#   parking purchase calculation loop
    while True:
        try:
            # user input loop & validation
            hoursParked = int(input("How many hours would you like to park? "))
            if hoursParked > 0:
                parkingSubtotal += hoursParked * hourlyRate
                print(f"Your current subtotal is ${parkingSubtotal:.2f}")

                # user input loop & validation
                repeatParkingInput = input("Would you like to add more hours to your parking? (y/n) ").lower()
                while repeatParkingInput != "y" and repeatParkingInput != "n":
                    print("Invalid input, please type y or n.")
                    repeatParkingInput = input("Would you like to add more hours to your parking? (y/n) ").lower()
                if repeatParkingInput == "n":
                    break
            else:
                    print("Please enter a number greater than 0.")
        except:
            print("Invalid input, please enter a whole number.")
    return parkingSubtotal


def taxCalculations(parkingSubtotal):
    taxAmount = parkingSubtotal * TAX_RATE
    return taxAmount


def totalCalculations(parkingSubtotal, taxAmount):
    total = parkingSubtotal + taxAmount
    return total


def printReceipt(parkingSubtotal, taxAmount, total):
    print("\n--- Receipt ---")
    print(f"Subtotal: ${parkingSubtotal:.2f}")
    print(f"Tax: ${taxAmount:.2f}")
    print(f"Parking Total: ${total:.2f}")


# module testing
# def main():
#     subtotal = parkingCalculations()
#     tax = taxCalculations(subtotal)
#     total = totalCalculations(subtotal, tax)
#     printReceipt(subtotal, tax, total)
#
# if __name__ == "__main__":
#     main()
