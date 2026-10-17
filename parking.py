'''
parking module
'''

def get_parking_time(prompt):
    '''
    gets the time in hours that people will be parked
    uses try-except to make sure bad input doesn't fail
    '''
    success = False
    while not success:
        try:
            time = int(input(prompt))
            success = True
        except:
            print("Invalid input. Try again")
    return time

def get_parking_cost(time, price_per_hour):
    '''
    returns the cost of parking
    takes time and an int in place of price_per_hour
    '''
    cost = time * price_per_hour
    return cost