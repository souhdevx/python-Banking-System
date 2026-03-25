import Signupfile as signup_module
import Loginfile as login_module

signup = signup_module.Signup()
login = login_module.Login(signup)

class Main:
    @staticmethod
    def menu():
        while True:
            print("-------------BANK-------------")
            print('1. Sign up')
            print('2. Login')
            print('3. Exit')
            print("-------------BANK-------------")
            choice = input('Enter your choice: ').strip()
            if choice == '1':
                signup.create_account()
            elif choice == '2':
                if login.login_user():
                    if login.menu():
                        print('Goodbye!')
                        break
            elif choice == '3':
                print('Goodbye!')
                break
            else:
                print('Please enter a valid choice!')

if __name__ == "__main__":
    Main.menu()
        