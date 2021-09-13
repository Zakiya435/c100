'''class car:
    def __init__(self,colour,company,speedLimit,model):
        self.colour = colour
        self.company = company
        self.speedLimit = speedLimit
        self.model = model

    def start(self):
        print("Your car has started")

    def stop(self):    
        print("YOur car has stopped")

    def crash(self):    
        print("Your car has crashed")

    def gear(self):
        print("You changed your gear")


tyre = car("red","Audi",120,"A6")

tyre.crash()
print(tyre.company)'''

class bank:
    def __init__(self,typeAcc,userId,bal):
        self.typeAcc = typeAcc
        self.userId = userId
        self.bal = bal

    def deposit(self):
        amount = int(input("Enter the amount to deposit"))
        self.bal = self.bal+amount
        print(self.bal)

one = bank("saving",123,1000)
one.deposit()