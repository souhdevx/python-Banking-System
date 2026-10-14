from random import *
class Signup:
    def __init__(self):
        self.accounts = []
    def create_account(self):
        account = {
            'username': input("Enter username: "),
            'password': input("Enter password: "),
            'balance': 0.0,
            'pin': 0000,
            'rib': 00000000
        }
        self.accounts.append(account)
        self.account = account
        print('Account created successfully.')
        print('Get your PIN code before login in!')
        return account
        

