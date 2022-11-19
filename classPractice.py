class Wallet:
    
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


if __name__ == "__main__":
    wallet_me = Wallet(300)
    wallet_other = Wallet() 
    wallet_me.show_funds()
    wallet_other.show_funds()
    print("Money paid: ")
    wallet_me.pay(20, wallet_other)
    wallet_me.show_funds()
    wallet_other.show_funds()
    print("Money deposited: ")
    wallet_me.deposit(10)
    wallet_me.show_funds()


        