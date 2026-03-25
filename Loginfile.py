class Login:
	def __init__(self, signup):
		# store reference to Signup instance so we can check accounts
		self.signup = signup
	def menu(self):
		while True:
			print("-------------We'll be happy to help you!-------------")
			print("1. Deposit: ")
			print("2. Withdraw: ")
			print("3. Account Balance: ")
			print("4. Exit: ")
			print("------------------------BANK------------------------")
			choice = input("Enter a valid choice: ").strip()
			if choice == '1':
				self.deposit()
			elif choice == '2':
				self.withdraw()
			elif choice == '3':
				self.balance()
			elif choice == '4':
				print('Thank you for using our bank. See you next time!')
				return True
			else:
				print("Invalid choice!!")
				continue
			return False

	def login_user(self):
		username = input("Enter username: ")
		password = (input("Enter password: "))
		for account in self.signup.accounts:
			if username == account['username'] and password == account['password']:
				try:
					last_step = int(input("Enter your id: "))
				except ValueError:
					print("ID must be numeric")
					return False
				if last_step != account['id']:
					print("Make sure that this is your account!")
					return False
				print(f"Welcome back, {username}!")
				return True
		print("Account not found or wrong credentials!")
		return False
	def deposit(self):
		try:
			add_founds = float(input("Enter amount to deposit: "))
		except ValueError:
			print('Enter a valid amount!')
			return
		try:
			self.id_check = int(input("Enter your id: "))
		except ValueError:
			print("ID should be numeric")
			return
		for account in self.signup.accounts:
			if self.id_check == account['id']:
				account['balance'] += add_founds
				print(f"_Deposited: {add_founds}$.\n_New balance: {account['balance']}$")
				return
		print("Invalid account!")
	def withdraw(self):
		try:
			withdraw_money = float(input("Enter amount to withdraw: "))
		except ValueError:
			print("Please enter a numeric amount")
			return
		try:
			self.id_check = int(input("Enter your id: "))
		except ValueError:
			print("ID should be numeric")
			return
		for account in self.signup.accounts:
			if self.id_check == account['id']:
				if withdraw_money > account['balance']:
					print("Not enough balance!")
					return
				else:
					account['balance'] -= withdraw_money
					print(f"_Withdrawn: {withdraw_money}$.\n_New balance: {account['balance']}$")
					return
		print("Invalid account!")
	def balance(self):	
		try:	
			self.id_check = int(input("Enter your id: "))
		except ValueError:
			print("ID should be numeric")
		for account in self.signup.accounts:
			if self.id_check == account['id']:
				print(f"Your current balance is {account['balance']}!")
				return
		print("Invalid account!")