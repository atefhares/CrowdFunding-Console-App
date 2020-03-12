#!python3
import auth
import project
from Constants import PARENT_DATABASE_PATH

users_file_path = PARENT_DATABASE_PATH + "/users.json"

projects_file_path = ""  # will be created after login


# ===================================================================

def prompt_system_choices():
    print("\n" * 3, "Select your choice: ")
    print("\t" * 2, "1- View all projects")
    print("\t" * 2, "2- Create a project")
    print("\t" * 2, "3- Edit a project")
    print("\t" * 2, "4- Delete a project")
    choice = input("")

    if choice.isdigit() and int(choice) in [1, 2, 3, 4]:
        if int(choice) == 1:
            project.print_all_projects(projects_file_path)
        elif int(choice) == 2:
            project.create_project(projects_file_path)
        elif int(choice) == 3:
            project.edit_project(projects_file_path)
        elif int(choice) == 4:
            project.delete_project(projects_file_path)

        print("\n" * 3)
        prompt_system_choices()
    else:
        print("\n" * 3)
        print("Enter valid choice!")
        prompt_auth_choices()


def init_projects_path(email):
    global projects_file_path
    projects_file_path = PARENT_DATABASE_PATH + "/" + email + ".json"


def prompt_login():
    email = input("Enter you email: ")
    password = input("Enter you password: ")
    if auth.login(users_file_path, email, password):
        init_projects_path(email)
        prompt_system_choices()
    else:
        print("Wrong credentials!!")
        prompt_auth_choices()


def prompt_auth_choices():
    print("Please select your choice: ")
    print("\t" * 2, "1- Register")
    print("\t" * 2, "2- login")
    choice = input("")
    if choice.isdigit() and int(choice) in [1, 2]:
        if int(choice) == 1:
            auth.register(users_file_path)
            prompt_auth_choices()
        elif int(choice) == 2:
            prompt_login()
    else:
        print("\n" * 3)
        print("Enter valid choice!")
        prompt_auth_choices()


print("*" * 5, "Welcome to Crowd-Funding console app", "*" * 5)
print(" " * 5, "This program is created by AtefHares.", " " * 5)
print("\n" * 2)

# ---------------------------------------------------------------
# ----------------- PROGRAM starts from HERE --------------------
# ---------------------------------------------------------------
prompt_auth_choices()
