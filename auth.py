import re
import json
from files_operations import is_file_empty, create_dir_if_not_exists
from Constants import PARENT_DATABASE_PATH


# -----------------------------------------------

def is_valid_name(arg):
    return re.search("^[a-zA-Z]+$", arg)


def is_valid_email(arg):
    return re.search(r"^[\w.+\-]+@[\w]+\.[a-z]+$", arg)


def is_valid_password(passwd, passwd_confirmation):
    if len(passwd) < 8:
        return False
    else:
        return passwd == passwd_confirmation


def is_valid_phone_number(arg):
    # validate these numbers only
    return re.search(r"^(010|011|012)[0-9]{8}$", arg)


# -----------------------------------------------

def read_first_name():
    first_name = input("Enter your first name: ")
    if not is_valid_name(first_name):
        print("Enter valid first name!")
        return read_first_name()
    return first_name


def read_last_name():
    last_name = input("Enter your last name: ")
    if not is_valid_name(last_name):
        print("Enter valid last name!")
        return read_last_name()
    return last_name


def read_email():
    email = input("Enter your email: ")
    if not is_valid_email(email):
        print("Enter valid email!")
        return read_email()
    return email


def read_password():
    password = input("Enter your password: ")
    password_confirmation = input("Confirm your password: ")
    if not is_valid_password(password, password_confirmation):
        print("Enter valid password! [at least 8 chars]")
        return read_password()
    return password


def read_phone_number():
    phone_number = input("Enter your phone number: ")
    if not is_valid_phone_number(phone_number):
        print("Enter valid phone_number!")
        return read_phone_number()
    return phone_number


# -----------------------------------------------

def get_all_users(users_file_path):
    if is_file_empty(users_file_path):
        return []
    else:
        file = None
        try:
            file = open(users_file_path, "r")
            return json.load(file)
        except Exception as e:
            print("[get_all_users] Exception: ", e)
        finally:
            if file is not None:
                file.close()


def user_already_registered(fl):
    pass


def create_new_user(users_file_path, user):
    all_users = get_all_users(users_file_path)

    file = None
    try:
        create_dir_if_not_exists(PARENT_DATABASE_PATH)
        file = open(users_file_path, "w")
        if not user_already_registered(file):
            all_users.append(user)
            file.write(json.dumps(all_users))
    except Exception as e:
        print("[create_new_user] Exception: ", e)
    finally:
        if file is not None:
            file.close()


def register(users_file_path):
    first_name = read_first_name()
    last_name = read_last_name()
    email = read_email()
    password = read_password()
    phone_number = read_phone_number()
    user = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password,
        "phone_number": phone_number
    }
    create_new_user(users_file_path, user)


def login(users_file_path, email_arg, pass_arg):
    if is_file_empty(users_file_path):
        return False
    else:
        all_users = get_all_users(users_file_path)
        for user in all_users:
            if user["email"] == email_arg and user["password"] == pass_arg:
                print("LoggedIn")
                return True
        return False
