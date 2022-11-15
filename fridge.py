class fridge:
    def __init__(self):
        self.NumberOfItems = 0
        self.DoorOpen = False
        self.isRunning = True
        
    def printFridge(self):
        print("Hello im a refridgerator with", self.NumberOfItems, "number of items,")
        if self.DoorOpen == False:
            print("and my door is closed.")
        else:
            print("and my door is open.")
            
        if self.isRunning == True:
            print("I am running.... better come catch me sloww aahhh")
        else:
            print("I am not running.... dont let your food spoil")
        
    def openDoor(self):
        self.DoorOpen = True
    def closeDoor(self):
        self.DoorOpen = False
        
    def fillFridge(self, num):
        if self.DoorOpen == True:
            self.NumberOfItems += num
            print("you just added", num,"foods to the fridge")
        else:
            print("you cant put dstuff into the fridge when the door is closed dum dum")
    
    def MakeDinner(self):
        if self.DoorOpen == True:
            self.NumberOfItems -= 10
            print("you made dinner and used 10 foods")
        else:
            print("you cant put dstuff into the fridge when the door is closed dum dum")
            
#--------------------------------------------------------------------------------------------
            
f1 = fridge()#calls the constructor
f1.printFridge()
print()
food = int(input("how much food to add?"))
f1.fillFridge(food)
print()
f1.openDoor()
f1.fillFridge(food)
f1.printFridge()
print()
f1.MakeDinner()
f1.closeDoor()
f1.printFridge()
