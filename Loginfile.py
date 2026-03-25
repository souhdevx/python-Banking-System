class Login:
    def __init__(self, signup):
        self.signup = signup

    def menu(self):
        while True:
            print("\n" + "-"*15 + " Welcome " + "-"*15)
            print("1. Deposit\n2. Withdraw\n3. Account Balance\n4. Logout")
            choice = input("Enter choice: ").strip()

            if choice == '1':
                self.deposit()
            elif choice == '2':
                self.withdraw()
            elif choice == '3':
                self.balance()
            elif choice == '4':
                print('Logging out...')
                return True 
            else:
                print("Invalid choice!!")

    def login_user(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        for account in self.signup.accounts:
            if username == account['username'] and password == account['password']:
                try:
                    last_step = int(input("Enter your id to confirm: "))
                except ValueError:
                    print("ID must be numeric")
                    return False
                if last_step != account['id']:
                    print("ID mismatch!")
                    return False
                print(f"Welcome back, {username}!")
                return True
        print("Invalid credentials!")
        return False

    def deposit(self):
        try:
            amount = float(input("Amount to deposit: "))
            user_id = int(input("Enter your id: "))
            for acc in self.signup.accounts:
                if acc['id'] == user_id:
                    acc['balance'] += amount
                    print(f"Success! New balance: {acc['balance']}$")
                    return
            print("Account not found!")
        except ValueError:
            print("Please enter numbers only.")

    def withdraw(self):
        try:
            amount = float(input("Amount to withdraw: "))
            user_id = int(input("Enter your id: "))
            for acc in self.signup.accounts:
                if acc['id'] == user_id:
                    if amount > acc['balance']:
                        print("Insufficient funds!")
                    else:
                        acc['balance'] -= amount
                        print(f"Success! New balance: {acc['balance']}$")
                    return
            print("Account not found!")
        except ValueError:
            print("Please enter numbers only.")

    def balance(self):
        try:
            user_id = int(input("Enter your id: "))
            for acc in self.signup.accounts:
                if acc['id'] == user_id:
                    print(f"Balance: {acc['balance']}$")
                    return
            print("Account not found!")
        except ValueError:
            print("Invalid ID.")
