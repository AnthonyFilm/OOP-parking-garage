class ParkingGarage():
    """
    This class establishes a simple way to initialize new garage ticketing systems and manage customers.
    Each object instantiated is a separate physical parking garage. 

    Upon instantiation of a new garage by the garage owner, the program asks for it's parking space capacity 
    and the amount you'd like to charge per parking space.
    WARNING: Don't exploit your customers by charging too much. Parking is a bear!

    After instantiation, the rest of the program is oriented toward your customers: 
    allowing them to get a parking ticket, park in an appropriate space, 
    pay for the ticket when leaving, and then confirming payment before exiting the garage. 

    """
    def __init__(self):
        print('Welcome to the Parking Garage Automation Program or PGAP')
        while True:
            try:
                self.numberSpaces = int(input('Please enter the number of parking spaces in your garage: '))
                self.amountPerSpace = float(input('Please enter the amount (in US dollars) that you would like to charge per parking space: '))
                break
            except:
                print('That is not a valid entry. Please enter a valid number.')
                continue
        self.parkingSpaces = [x for x in range(self.numberSpaces)]
        self.spacesAvalible = len(self.parkingSpaces)
        self.tickets = [x for x in range(self.numberSpaces)]
        input('Your garage ticketing sofware has been initialized. Ready to receive customers. Press ENTER to continue.')
        print('\n\n\n\n')
        
    def press_enter(self):
        input(f'\nPress ENTER to continue. ')

    def takeTicket(self):
        print(f'Welcome to the garage. There are {self.spacesAvalible} parking spaces available.  Please take a ticket. ')
        self.currentTicket = {}
        self.currentTicket['ticket_number'] = self.tickets.pop()
        self.currentTicket['space_number'] = self.parkingSpaces.pop()  
        self.currentTicket['paid'] =  False
        self.currentTicket['amount_paid'] = 0.0
        input(f"Your ticket number is {self.currentTicket['ticket_number']}. Please proceed to parking space {self.currentTicket['space_number']}. Press ENTER to continue.")
  
    def payForParking(self):
        print('\n\nBefore exiting the garage, please pay your ticket here.')
        while True:
            try:
                payment = float(input(f"You owe ${self.amountPerSpace - self.currentTicket['amount_paid']}. Please enter the payment amount. "))
            except:
                print('That is not a valid entry. Please try again.')
                self.press_enter()
                continue    
            self.currentTicket['amount_paid'] += payment
            if self.currentTicket['amount_paid'] == self.amountPerSpace: 
                print('Your ticket has been paid. You have 15 minutes to leave... \n...or we will eliminate you. (Just kidding...or are we?)')
                self.currentTicket['paid'] = True
                self.press_enter()
                break
            elif self.currentTicket['amount_paid'] > self.amountPerSpace:
                print(f"You have overpaid. Please take your change of ${self.currentTicket['amount_paid'] - self.amountPerSpace}. \nYour ticket has been paid. You have 15 minutes to leave.")
                self.currentTicket['paid'] = True
                self.press_enter()
                break
            else:
                print(f'You have under paid.', end = " ")
                continue
        
    def leaveGarage(self):
        print('You are now leaving the garage. Warning: you must pay again to leave and reenter.')
        self.press_enter()
        if self.currentTicket['paid'] == True:
            print('Thank You, have a nice day')
            self.parkingSpaces.append(self.currentTicket['space_number'])
            self.tickets.append(self.currentTicket['ticket_number'])
        else:
            self.payForParking()



my_garage = ParkingGarage()

my_garage.takeTicket()

my_garage.payForParking()

my_garage.leaveGarage()