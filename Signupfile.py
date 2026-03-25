from random import randint

class Signup:
    def __init__(self):
        self.accounts = []

    def create_account(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        user_id = randint(1000, 9999)

        new_account = {
            'username': username,
            'password': password,
            'balance': 0.0,
            'id': user_id
        }
        
        print(f"Your ID is {user_id}. Keep it safe!")
        self.accounts.append(new_account)
