# Creates computer objects that store information on themselves and can retrieve and manipulate necessary information for the resale shop
class Computer:

    
    description: str # Describes computer
    processor_type: str # What processor the computer has
    hard_drive_capacity: int # The capacity of the hard drive
    memory: int # The memory capacity
    operating_system: str # The operating system currently
    year_made: int # The year it was made
    price: int # The price it is being reselled for

     # Constructs a computer object and initializes its attributes
    def __init__ (self, description: str, processor_type: str, hard_drive_capacity: int, memory: int, operating_system: str, year_made: int, price: int):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price


     # Allows other files to access the computer object
    def getComputer(self):
         return self

    # Allows other files to access the description
    def getDescription(self):
         return self.description
    
    # Allows other files to access the operating system
    def getOperating_System(self):
         return self.operating_system
    
    # Allows other files to access the year made
    def getYear(self):
         return self.year_made
    
    # Allows other files to access the price
    def getPrice(self):
         return self.price
    
    # Allows the computer object to change its own price
    def changePrice(self, new_price):
         self.price = new_price
    
    # Allows the computer object to change its own operating system
    def changeOS(self, new_os):
         self.operating_system = new_os

     # Allows the computer object to be tested
    def __str__(self) -> str:
         return "Desc: " + self.description + "\n" + "Processor: " + self.processor_type + "\n" "HD: " + str(self.hard_drive_capacity) + "\n" + "Memory: " + str(self.memory) + "\n" + "OS: " + self.operating_system + "\n" + "Year: " + str(self.year_made) + "\n" + "Price: " + str(self.price)

   

def main():
     # Create a computer
        my_computer = Computer("Mac Pro (Late 2013)",
    "3.5 GHc 6-Core Intel Xeon E5",
    1024, 64,
    "macOS Big Sur", 2013, 1500)
     
     # Test all methods with print statements
        print(my_computer.getOperating_System())
        print(my_computer.getYear())
        print(my_computer.getPrice())
        my_computer.changePrice(30)
        print(my_computer.getPrice())
        
        # Test computer object
        print(my_computer.__str__())


main()
