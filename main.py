from classes import Hospital, Doctor, Patient, Nurse
from hospital_functions import create_hospital, create_patient, create_doctor
from menus import main_menu, add_menu, search_menu, remove_menu

def main():
    # display message
    print("----Hospital Management System----")
    print("Create a new Hospital...")

    hospital = create_hospital()

    print("a new hospital created...")

    main_menu(hospital)

if __name__ == "__main__":
    main()