
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
        else:
            print("That is not a valid response! Please pick one from the list")

run()