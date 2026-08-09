from hospital_functions import create_doctor, create_patient, create_nurse
from hospital_functions import display_person
from hospital_functions import id_validator

def main_menu(hospital):

    while True:
        print("-----MAIN MENU-----")
        print("1. Add a person")
        print("2. Remove a person")
        print("3. Search a person")
        print("4. Display a person")
        print("5. Exit")

        choice = input("Enter your choice: ")
        match choice:
            case '1':
                add_menu(hospital)

            case '2':
                remove_menu(hospital)

            case '3':
                search_menu(hospital)

            case '4':
               display_menu(hospital)

            case '5':
                print("thank you!")
                break

            case _:
                print("invalid option!")
                continue


def add_menu(hospital):
    while True:
        print("-----ADD A PERSON-----")
        print("1. Add a doctor")
        print("2. Add a patient")
        print("3. Add a nurse")
        print("4. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case '1':
                create_doctor(hospital)
            case '2':
                create_patient(hospital)
            case '3':
                create_nurse(hospital)
            case '4':
                break
            case _:
                pass


def remove_menu(hospital):
    while True:
        print("-----REMOVE A PERSON-----")
        print("1. Remove a doctor")
        print("2. Remove a patient")
        print("3. Remove a nurse")
        print("4. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case '1':
                pass
            case '2':
                pass
            case '3':
                pass
            case '4':
                break
            case _:
                pass


def search_menu(hospital):
    while True:
        print("-----SEARCH A PERSON-----")
        print("1. Search a doctor")
        print("2. Search a patient")
        print("3. Search a nurse")
        print("4. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case '1':
                pass
            case '2':
                pass
            case '3':
                pass
            case '4':
                break
            case _:
                pass


def display_menu(hospital):
    while True:
        print("-----DISPLAY A PERSON-----")
        print("1. Display a doctor")
        print("2. Display a patient")
        print("3. Display a nurse")
        print("4. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case '1':
                display_menu_person(hospital, "doctor")
                # display_doctor(hospital)
            case '2':
                display_menu_person(hospital, "patient")
                # display_patient(hospital)
            case '3':
                display_menu_person(hospital, "nurse")
                # display_nurse(hospital)
            case '4':
                break
            case _:
                pass


def display_menu_person(hospital, person):
    print(f"--------DISPLAY {person}--------")
    print(f"1. Display a {person} using ID")
    print(f"2. Display all {person}s")

    choice = input("Enter your choice: ")

    match choice:
        case '1':
            while True:
                person_id = input(f"Enter {person} id: ")
                is_available, person_object = id_validator(hospital, person_id, person)
                if is_available:
                    person_object.display()
                    break
        case '2':
            display_person(hospital, person)
