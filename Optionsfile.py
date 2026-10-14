from random import randint
import Signupfile

class Options:
    def __init__(self, signup):
        self.signup = signup

    def pin_code(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        account = None
        for acc in self.signup.accounts:
            if acc['username'] == username and acc['password'] == password:
                account = acc
                break
        if account is None:
            print("Account not found.")
            return
        pin_numbers = randint(1000, 9999)
        account['pin'] = pin_numbers
        print(f"Your PIN Code is {pin_numbers}, Make sure that nobody sees it!")

    def rib(self):
        username = input("Enter your username: ")
        account = None
        for acc in self.signup.accounts:
            if acc['username'] == username:
                account = acc
                break
        if account is None:
            print("Account not found.")
            return
        rib_numbers = randint(10000000, 99999999)
        account['rib'] = rib_numbers
        print(f"Your RIB is {rib_numbers}.")

    def menu(self):
        while True:
            print("-------------BANK-------------")
            print('1. PIN Code')
            print('2. RIB')
            print('3. Exit')
            print("-------------BANK-------------")
            choice = input("Enter your choice: ").strip()
            if choice == '1':
                self.pin_code()
            elif choice == '2':
                self.rib()
            elif choice == '3':
                break
            else:
                print('Please enter a valid choice!')
            
