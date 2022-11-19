#Player Class

class Player:
    def __init__(self, name:str, wallet:Shop) -> None:
        self.hp = 100
        self.inventory = []
        # self.wallet = Shop_Sells

    def get_health(self): #retrieving the health of player
        pass
    def alive(self):
        if self.hp > 0:
            return True   
        else:
            self.hp = 0
            return False

    def get_inventory(): #retrieving inventory of player (list)
        pass



#Im making an enemy        
'''
class Enemy:
# health
# inventory
'''

#I'm making a list of inventory to use ?
'''
class Inventory():
'''

#I'm making a store to buy and sell items
'''
class Shop:
    def __init__(self, money = 0) -> None:
        self.money = money

    def deposit(self, amount):
        self.money += amount

    def pay(self, amount:int, wallet):
        if amount <= self.money:
            self.money -= amount
            wallet.deposit(amount)
        else:
            print("Not enough funds")
    
    def show_funds(self):
        print(f"The current balance ${self.money}")
'''

#I'm making a wallet for each player to use from
'''
 class Person:
    def __init__(self, name:str, age:int, wallet = Wallet(),job:str|None = None) -> None:
        self.name = name
        self.age = age
        self.wallet = wallet 
        self.job = job

    def get_wallet(self):
        return self.wallet

    def about(self):
        print(f"{self.name}\n{self.age}\n{self.job}")
        self.wallet.show_funds()

    def say(self, message):
        print(f"{self.name}: \"{message}\"")
'''