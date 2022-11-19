from classPractice import Wallet

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

        