'''
parking module
'''

def get_parking_time(prompt):
    success = False
    while not success:
        try:
            time = int(input(prompt))
            success = True
        except:
            print("Invalid input. Try again")
    return time

def get_parking_cost(time, price_per_hour):
    cost = time * price_per_hour
    return cost