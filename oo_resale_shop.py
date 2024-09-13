from computer import *

class ResaleShop:

    # What attributes will it need?
    inventory : list = []

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory = []
        

    # What methods will you need?

    # Allows computers to be bought if that computer has not been bought before
    def buy(self, buying_computer):
        if buying_computer in self.inventory:
            print("We have already purchased this computer.")
        else:
            self.inventory.append(buying_computer)
            print("We successfully bought this computer.")

    # Allows computers to be sold if that computer is in stock
    def sell(self, selling_computer):
        if selling_computer in self.inventory:
            self.inventory.remove(selling_computer)
            print("This computer has been sold!")
        else:
            print("This computer is not in stock")
    
    def updatePrice(self, new_price: int, updating_computer):
        if updating_computer in self.inventory:
            updating_computer.price = new_price
            print(updating_computer, "price is updated to", new_price)
        else:
            print("Computer not found.")
    
    def refurbish(self, refurbish_computer):
        if refurbish_computer in self.inventory:
            temp_price : int = refurbish_computer.getPrice()
            if temp_price < 2000:
                ResaleShop.updatePrice(refurbish_computer, 0)
            elif temp_price < 2014:
                ResaleShop.updatePrice(refurbish_computer, 250)




    
        
        
        
        
        
def main():
    my_ResaleShop: ResaleShop = ResaleShop()
    my_computer = Computer(
    "Mac Pro (Late 2013)",
    "3.5 GHc 6-Core Intel Xeon E5",
    1024, 64,
    "macOS Big Sur", 2013, 1500
    )
    my_ResaleShop.buy(my_computer)
    my_ResaleShop.buy(my_computer)
    my_ResaleShop.sell(my_computer)
    my_ResaleShop.sell(my_computer)


main()