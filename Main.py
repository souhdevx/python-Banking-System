import Signupfile 
import Loginfile
import Optionsfile

signup = Signupfile.Signup()
login = Loginfile.Login(signup)
options = Optionsfile.Options(signup)

class Main:
    @staticmethod
    def menu():
        while True:
            print("-------------BANK-------------")
            print('1. Sign up')
            print('2. Login')
            print('3. Other Options')
            print('4. Exit')
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
                options.menu()
            elif choice == '4':
                print('Goodbye!')
                break
            else:
                print('Please enter a valid choice!')

if __name__ == "__main__":
    Main.menu()
        
        
