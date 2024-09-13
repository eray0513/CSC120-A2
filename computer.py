class Computer:

    # What attributes will it need?
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__ (self, description: str, processor_type: str, hard_drive_capacity: int, memory: int, operating_system: str, year_made: int, price: int):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price


    # What methods will you need?

     # Allows other files to access the computer object
    def getComputer(self):
         return self

    # Allows other files to access the description
    def getDescription(self):
         return self.description
    
    # Allows other files to access the operating system
    def getOperating_System(self):
         return self.operating_system
    
    #Allows other files to access the year made
    def getYear(self):
         return self.year_made
    
    #Allows other files to access the price
    def getPrice(self):
         return self.price
    
    def changePrice(self, new_price):
         self.price = new_price
    
    def changeOS(self, new_os):
         self.operating_system = new_os

  
         
         
         

def main():
        my_computer = Computer("Mac Pro (Late 2013)",
    "3.5 GHc 6-Core Intel Xeon E5",
    1024, 64,
    "macOS Big Sur", 2013, 1500)
        print(my_computer.getOperating_System())
        print(my_computer.getYear())
        print(my_computer.getPrice())
        my_computer.changePrice(30)
        print(my_computer.getPrice())


main()
