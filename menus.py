from hospital_functions import create_doctor, create_patient, create_nurse
from hospital_functions import display_person
from hospital_functions import id_validator
from hospital_functions import search_by_id, remove_person

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
        print("4. Back")

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
                print("Enter a valid option!")


def remove_menu(hospital):
    while True:
        print("-----REMOVE A PERSON-----")
        print("1. Remove a doctor")
        print("2. Remove a patient")
        print("3. Remove a nurse")
        print("4. Back")

        choice = input("Enter your choice: ")

        match choice:
            case '1':
                person = 'doctor'
            case '2':
                person = 'patient'
            case '3':
                person = 'nurse'
            case '4':
                break
            case _:
                print("Enter a valid option!")
                continue

        while True:
            person_id = input(f"Enter {person} ID / Q to quit: ")
            if person_id in ('Q', 'q'):
                break
            if id_validator(hospital, person_id, person):
                remove_person(hospital, person_id, person)

def search_menu(hospital):
    person = None
    while True:
        print("-----SEARCH A PERSON-----")
        print("1. Search a doctor")
        print("2. Search a patient")
        print("3. Search a nurse")
        print("4. Back")

        choice = input("Enter your choice: ")

        match choice:
            case '1':
                person = 'doctor'
            case '2':
                person = 'patient'
            case '3':
                person = 'nurse'
            case '4':
                break
            case _:
                print("Enter a valid option!")
                continue

        while True:
            person_id = input(f"Enter {person} ID / Q to quit: ")
            if person_id in ('Q', 'q'):
                break
            is_available, person_object = search_by_id(hospital, person_id, person)
            if is_available:
                person_object.display()
                break

def display_menu(hospital):
    while True:
        print("-----DISPLAY A PERSON-----")
        print("1. Display a doctor")
        print("2. Display a patient")
        print("3. Display a nurse")
        print("4. Back")

        choice = input("Enter your choice: ")

        match choice:
            case '1':
                display_menu_person(hospital, "doctor")
            case '2':
                display_menu_person(hospital, "patient")
            case '3':
                display_menu_person(hospital, "nurse")
            case '4':
                break
            case _:
                print("enter a valid option!")


def display_menu_person(hospital, person):
    print(f"--------DISPLAY {person}--------")
    print(f"1. Display a {person} using ID")
    print(f"2. Display all {person}s")

    choice = input("Enter your choice: ")

    match choice:
        case '1':
            while True:
                person_id = input(f"Enter {person} ID / Q to quit: ")
                if person_id in ('Q', 'q'):
                    break
                is_available, person_object = id_validator(hospital, person_id, person)
                if is_available:
                    person_object.display()
                    break
        case '2':
            display_person(hospital, person)
        case _:
            print("Enter a valid option!")
