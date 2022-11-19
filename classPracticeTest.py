from classPractice import Wallet
from personClass import Person

if __name__ == "__main__":
    print("\n Info: ")
    person_Mila = Person("Mila", 21, Wallet(1))
    person_William = Person("William", 22, Wallet(2967), "Computer Science")
    person_Mila.about()
    print()
    person_William.about()
    print("\n Text: ")
    person_Mila.say("Give me $300.")
    person_William.say("Please dont hurt me. Take my money.")
    print("\n Hold-up: ")
    person_William.get_wallet().pay(20, person_Mila.wallet)
    person_Mila.about()
    person_William.about()

