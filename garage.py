
class parkingGarage():

    tickets = [1,1,1,1,1]
    parkingSpaces = [1,1,1,1,1]
    currentTicket = {1 : 'paid'}

    def __init__(self,tickets, parkingSpaces, currentTicket):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket

    def takeTicket(self):
        if self.tickets == []:
            print("Sorry there are no more available parking spaces.")
        else:
            print("Please take the ticket")
            self.tickets.remove(1)
            self.parkingSpaces.remove(1)

    def payForParking(self):
        insertTicket = int(input("Please insert your ticket and enter the amount that you have paid if you prepaid: "))
        if insertTicket != 0:
            print("Your ticket has been paid, and you have 15 minutes to exit the garage.")
            self.currentTicket[1] = True
        else:
            print("\nPlease insert your payment method")
            self.currentTicket[1] = True
    
    def leaveGarage(self):

        for key in self.currentTicket:
            if (self.currentTicket[key] == True):
                print("Thank you have a nice day")
                self.tickets = self.tickets.append(1)
                self.parkingSpaces = self.parkingSpaces.append(1)
            else: 
                print("Please input your payment method")
                self.tickets = self.tickets.append(1)
                self.parkingSpaces = self.parkingSpaces.append(1)


parking = parkingGarage([1,1,1,1,1], [1,1,1,1,1], {1: 'paid'})
parking.takeTicket()
parking.payForParking()
parking.leaveGarage()
        




