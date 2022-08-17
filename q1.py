# Create a class called cart that retains items and has methods to add, remove, and show

class Cart():
    def __init__(self, spotsTaken, spotsAvailable, speed, color):
        self.spotsTaken = spotsTaken
        self.spotsAvailable = spotsAvailable
        self.speed = speed
        self.color = color
    
    def loadItems(self):
        if self.spotsAvailable <= 0:
            print("The cart is full. I hope you can carry stuff in your arms because nothing else is fitting in here")
        else:
            items = int(input("How many items are you adding?" ))
            self.spotsAvailable -= items
            self.spotsTaken += items
            print(f"{items} items have been stacked in the cart. There are {self.spotsAvailable} spots available")
            print(f"spotsAvailable: {self.spotsAvailable}")
            print(f"spotsTaken: {self.spotsTaken}")
    
    def lessItems(self):
        if self.spotsAvailable == 0:
            print("There are no items left to remove!")
            print(f"spotsAvailable: {self.spotsAvailable}")
            print(f"spotsTaken: {self.spotsTaken}")
            self.spotsAvailable = self.spotsTaken
        else:
            remove = int(input("How many items are you removing? "))
            self.spotsAvailable += remove
            self.spotsTaken -= remove
            if self.spotsAvailable >= self.spotsTaken:
                # self.spotsAvailable = self.spotsTaken
                print(f"{remove} items have been removed. There are {self.spotsAvailable} spots left in the cart.")
                print(f"spotsAvailable: {self.spotsAvailable}")
                print(f"spotsTaken: {self.spotsTaken}")
            # print(f"{remove} items have been removed. There are {self.spotsAvailable} spots left in the cart.")

    def changeSpeed(self):
        change = input("How fast do you want to go? ")
        self.speed = change
        print(f"You are now traveling at {self.speed}/mph")
        
    def checkSpots(self):
        print(self.spotsAvailable)
    
    def admireCart(self):
        print(f"Would ya just look at that beautiful, shiny {self.color} shopping cart!")
        

nickCart = Cart(0, 40, 45, 'hot pink')

def run():
    while True:
        response = input('What would you like to do? Load/Unload/Change Speed/Check Spots/Admire/Quit: ')
        if response.lower() == 'quit':
            print("Did you pay for those items? Hello? Cash or credit? :(")
            break
        elif response.lower() == 'load':
            nickCart.loadItems()
        
        elif response.lower() == 'unload':
            nickCart.lessItems()
            
        elif response.lower() == 'change speed':
            nickCart.changeSpeed()
        
        elif response.lower() == 'check spots':
            nickCart.checkSpots()
        
        elif response.lower() == "admire":
            nickCart.admireCart()
        
        else:
            print("That is not a valid response! Please pick one from the list")

run()