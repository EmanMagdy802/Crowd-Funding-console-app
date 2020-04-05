from Authentication import registration
from Authentication import login


def main_menu():
    while True:
        print("-------- Main Menu ----------")

        choice = int(input("""
        Choose if you want to login or register:
        1| Register
        2| LogIn
        3| Exit
        """))

        if choice == 1:
            registration.register()
        elif choice == 2:
            login.login_menu()
        elif choice == 3:
            exit()


print('      CROWD-FUNDING App')
main_menu()
