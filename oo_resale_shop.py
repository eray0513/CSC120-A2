# Import computer object class
from computer import *

# Import optional from typing
from typing import Optional

class ResaleShop:


    # Sets up the inventory as a list
    # Inventory keeps track of the computers that the resale shop owns
    inventory : list = []


    # Creates a Resale Shop Object and initializes its inventory to empty
    def __init__(self):
        self.inventory = []


    # Prints a banner when the shop is open for business
    def open(self):
        print("-" * 21)
        print("COMPUTER RESALE STORE")
        print("-" * 21)

    # Allows computers to be bought if that computer has not been bought before
    def buy(self, buying_computer):
        if buying_computer in self.inventory: # Checks if computer is in stock
            print("We have already purchased this computer.")
        else:
            self.inventory.append(buying_computer) # Adds the computer to inventory
            print("We successfully bought this computer.")

    # Allows computers to be sold if that computer is in stock
    def sell(self, selling_computer):
        if selling_computer in self.inventory: # Checks if the computer is in stock
            self.inventory.remove(selling_computer) # Removes the computer from inventory
            print("This computer has been sold!")
        else:
            print("This computer is not in stock")
    
    # Allows resale shop to update the computer price
    def updatePrice(self, updating_computer, new_price : int):
        if updating_computer in self.inventory: # Checks if the computer is in stock
            updating_computer.changePrice(new_price) # Call to method in computer class
            print("This computer's price is updated to $", updating_computer.getPrice())
        else:
            print("Computer not found.")

    # Allows the resale shop to print and check its inventory
    def printInventory(self): 
        if self.inventory: # Checks if their is anything in the inventory
            for i in self.inventory:
                print("Inventory:")
                print(i.getDescription()) # Call to method in computer class
                print()
        else:
            print("No inventory found.")

    # Allows the resale shop to refurbish a new computer by setting its price and updating the OS
    def refurbish(self, refurbish_computer, new_os: Optional[str] = None):
        if refurbish_computer in self.inventory: # Checks if the computer is in stock
            temp_year : int = refurbish_computer.getYear()
            if temp_year < 2000:
                self.updatePrice(refurbish_computer, 0) # Donate computers older than 25 years
            elif temp_year < 2014:
                self.updatePrice(refurbish_computer, 250) # Large discount on 10+ year old computers
            elif temp_year < 2018:
                self.updatePrice(refurbish_computer, 550) # Medium discount on 6+ year old computers
            else:
                self.updatePrice(refurbish_computer, 1000) # Newer computers least discounted

            if new_os is not None: # Checks if there is a more up-to-date OS
                refurbish_computer.changeOS(new_os) # Installs/updates the OS of the computer object

        else:
            print("Computer not found")



        
        
        
        
        
def main():
    my_ResaleShop: ResaleShop = ResaleShop()
    my_computer = Computer(
    "Mac Pro (Late 2013)",
    "3.5 GHc 6-Core Intel Xeon E5",
    1024, 64,
    "macOS Big Sur", 2013, 1500
    )

    my_ResaleShop.open()
    my_ResaleShop.printInventory()
    my_ResaleShop.buy(my_computer)
    my_ResaleShop.printInventory()
    my_ResaleShop.buy(my_computer)
    my_ResaleShop.sell(my_computer)
    my_ResaleShop.sell(my_computer)
    
    my_computer2 = Computer(
    "Mac Pro (Late 2013)",
    "3.5 GHc 6-Core Intel Xeon E5",
    1024, 64,
    "macOS Big Sur", 2013, 1500
    )

    my_ResaleShop.buy(my_computer2)
    new_OS : str = "MACOS 3000"
    my_ResaleShop.refurbish(my_computer2, new_OS)
    my_ResaleShop.refurbish(my_computer2)
    my_ResaleShop.updatePrice(my_computer2, 3700)
    print(my_computer2.getPrice())
    print(my_computer2.getOperating_System())
    my_ResaleShop.updatePrice(my_computer2, 30)
    


main()