
# File

def open_project(file):
    try:
        # Open file
        pass
    except Exception:
        print("could not open file, please specify another file.")


def open_project_menu():
    file = input("Enter project definition file path")
    project = open_project(file)
    if not project:
        open_project_menu()
    return project


def main():
    project = open_project_menu()


if __name__ == '__main__':
    main()
