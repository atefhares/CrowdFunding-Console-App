import datetime
import json
from files_operations import is_file_empty, create_dir_if_not_exists
from Constants import PARENT_DATABASE_PATH


# ===============================================

def validate_date(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        # raise ValueError("Incorrect data format, should be YYYY-MM-DD")
        return False


def is_valid_date(arg):
    if not validate_date(arg):
        # if not re.search("([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))", arg):
        return False
    if datetime.datetime.strptime(arg, '%Y-%m-%d') < datetime.datetime.now():
        return False
    return True


# ===============================================

def print_all_projects(projects_file_path):
    all_projects = get_all_projects_list(projects_file_path)
    if len(all_projects) == 0:
        print("No projects found!")
        return
    for project in all_projects:
        print(project)


def is_project_exists(projects_file_path, project_title):
    all_projects = get_all_projects_list(projects_file_path)
    if len(all_projects) == 0:
        return False
    for project in all_projects:
        if project["title"] == project_title:
            return True
    return False


def get_all_projects_list(projects_file_path):
    if is_file_empty(projects_file_path):
        return []
    else:
        fl = None
        try:
            fl = open(projects_file_path, "r")
            return json.loads(fl.read())
        except Exception as e:
            print("[get_all_projects_list] Exception: ", e)
        finally:
            if fl is not None:
                fl.close()


# ===================================================================

def read_project_details():
    inp = input("Enter project details: ")
    return inp


def read_project_total_target():
    inp = input("Enter total target: ")
    if not inp.isdigit():
        print("Enter valid total target!")
        return read_project_total_target()
    return inp


def read_project_start_date():
    inp = input("Enter start date: ")
    if not is_valid_date(inp):
        print("Enter valid start date")
        return read_project_start_date()
    return inp


def read_project_end_date():
    inp = input("Enter end date: ")
    if not is_valid_date(inp):
        print("Enter valid end date")
        return read_project_end_date()
    return inp


# ===================================================================

def create_project(projects_file_path):
    title = input("Enter project Title: ")

    if is_project_exists(projects_file_path, title):
        print("Project exists!")
        return

    all_projects = get_all_projects_list(projects_file_path)

    details = read_project_details()
    total_target = read_project_total_target()
    start_date = read_project_start_date()
    end_date = read_project_end_date()

    project = {
        "title": title,
        "details": details,
        "total_target": total_target,
        "start_date": start_date,
        "end_date": end_date,
    }

    all_projects.append(project)

    fl = None
    try:
        create_dir_if_not_exists(PARENT_DATABASE_PATH)
        fl = open(projects_file_path, "w")
        fl.write(json.dumps(all_projects))
    except Exception as e:
        print("[create_project] Exception: ", e)
    finally:
        if fl is not None:
            fl.close()


def edit_project(projects_file_path):
    project_title = input("Enter project title: ")

    if not is_project_exists(projects_file_path, project_title):
        print("Project not exists!")
        return

    all_projects = get_all_projects_list(projects_file_path)
    for project in all_projects:
        if project["title"] == project_title:
            select = input("Edit details? [y/n]")
            if select == "y":
                project["details"] = input("Enter project's new details: ")
            select = input("Edit total_target? [y/n]")
            if select == "y":
                project["total_target"] = input("Enter project's new total_target: ")
            select = input("Edit start_date? [y/n]")
            if select == "y":
                project["start_date"] = input("Enter project's new start_date: ")
            select = input("Edit end_date? [y/n]")
            if select == "y":
                project["end_date"] = input("Enter project's new end_date: ")

            fl = None
            try:
                fl = open(projects_file_path, "w")
                fl.write(json.dumps(all_projects))
            except Exception as e:
                print("[create_project] Exception: ", e)
            finally:
                if fl is not None:
                    fl.close()
            break


def delete_project(projects_file_path):
    project_title = input("Enter project title: ")

    if not is_project_exists(projects_file_path, project_title):
        print("Project not exists!")
        return

    all_projects = get_all_projects_list(projects_file_path)
    for project in all_projects:
        if project["title"] == project_title:
            all_projects.remove(project)

            fl = None
            try:
                fl = open(projects_file_path, "w")
                fl.write(json.dumps(all_projects))
            except Exception as e:
                print("[create_project] Exception: ", e)
            finally:
                if fl is not None:
                    fl.close()

            break
