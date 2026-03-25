from random import *
class Signup:
    def __init__(self):
        self.accounts = []
    def create_account(self):
        self.account = {
            'username': input("Enter username: "),
            'password': (input("Enter password: ")),
            'balance': 0.0,
            'id': 0000
        }
        numbers = randint(1000, 9999)
        self.user_id = numbers
        if self.account['id'] != self.user_id:
            print(f"Your ID is {self.user_id}, Make sure that no body see it!")
            self.account['id'] = self.user_id
        else:
            return numbers
        self.accounts.append(self.account)    
        