from Projects import create_project
from Projects import list_projects
from Projects import edit_project
from Projects import delete_project


def get_user(email, password):
    with open("../users.txt", "r") as lines:
        lines = lines.readlines()
    flag = False
    for line in lines:
        split_intro = line.split(':')
        if split_intro[2] == email and split_intro[3] == password:
            flag = True
            user = {"First_Name": split_intro[0],
                    "Last_Name": split_intro[1],
                    "Email": split_intro[2],
                    "Password": split_intro[3],
                    "Mobile": split_intro[4],
                    }

    if flag:
        return user
    return {}


def login():
    email = input("Email: ")
    password = input("Password: ")
    user = get_user(email, password)
    if user:
        print("you are logged in!")
        return email
    else:
        print("Login Failed!")
        return 0


def login_menu():
    print("--------------- Log-In --------------------")
    user_mail = login()
    if user_mail:
        while True:
            choice = int(input("""
                Enter your choice:
                1- Create new project
                2- View all projects
                3- Edit project
                4- Delete project
                5- Exit
                """))

            if choice == 1:
                create_project.create_project(user_mail)
            elif choice == 2:
                list_projects.view_all_projects()
            elif choice == 3:
                edit_project.edit_project(user_mail)
            elif choice == 4:
                delete_project.delete_project(user_mail)
            elif choice == 5:
                return 0
