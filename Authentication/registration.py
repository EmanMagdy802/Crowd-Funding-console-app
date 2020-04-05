import re


def validate_name(is_last):
    if is_last:
        name = input("Last Name: ")
    else:
        name = input("First Name: ")

    if name.replace(" ", "").isalpha():
        return name
    else:
        print("invalid name!")
        return 0


def validate_email():
    while True:
        email = input("Email: ")
        email_regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
        if not email_regex.match(email):
            print("Invalid email! please enter a valid one")
        else:
            return email


def validate_password():
    while True:
        password = input("Enter a password: ")
        if len(password) < 8:
            print("Make sure your password is at lest 8 letters")
        elif re.search('[0-9]', password) is None:
            print("Make sure your password has a number in it")
        elif re.search('[A-Z]', password) is None:
            print("Make sure your password has a capital letter in it")
        else:
            return password


def confirm_password(correct_password):
    confirmed_password = input("Confirm Password: ")
    if confirmed_password == correct_password:
        return True
    return False


def validate_phone():
    while True:
        mobile_phone = input("Mobile Phone: ")
        mobile_regex = re.compile(r"^020?[10,11,12]\d{8}")
        if not mobile_regex.match(mobile_phone):
            print("Invalid phone number! please enter a valid password")
        else:
            return mobile_phone


def add_user(**kwargs):
    f = open("../users.txt", 'a')
    f.write(":".join([kwargs["First_Name"],
                      kwargs["Last_Name"],
                      kwargs["Email"],
                      kwargs["Password"],
                      kwargs["Mobile"],
                      ]))
    f.write('\n')
    f.close()


def get_user_name():
    pass


def create_user():
    first_name = validate_name(0)

    if first_name:
        last_name = validate_name(1)
        if last_name:
            email = validate_email()
            if email:
                password = validate_password()
                if password:
                    phone = validate_phone()
                    if phone:
                        new_user = {"First_Name": first_name,
                                    "Last_Name": last_name,
                                    "Email": email,
                                    "Password": password,
                                    "Mobile": phone}
                        return new_user
    return False


def register():
    user_data = create_user()
    if user_data:
        add_user(**user_data)
        print(user_data)
        print("Registration Succeeded :D ")
    else:
        print("Registration Failed -_- ")
