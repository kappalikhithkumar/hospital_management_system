from classes import Hospital, Doctor, Patient, Nurse


def id_validator(hospital, person_id, person):
    is_quadra = False
    is_digit = False
    is_unique = False
    is_valid = False

    if not person_id.isdigit():
        print("ID must be in digits")
        return is_digit
    is_digit = True

    if not len(person_id) == 4:
        print("ID length must be equal to 4")
        return is_quadra
    is_quadra = True

    if not person_id[0] in ('2','3','4'):
        if person == "doctor":
            print("doctor ID must start with 2")
        elif person == "nurse":
            print("nurse ID must start with 3")
        else:
            print("patient ID must start with 4")
        return False

    match person:
        case "doctor":
            if person_id[0] == '2':
                is_valid = True

        case "nurse":
            if person_id[0] == '3':
                is_valid = True

        case "patient":
            if person_id[0] == '4':
                is_valid = True

    if  hospital.has_id(person_id, person):
        print("ID must be unique")
        return is_unique
    is_unique = True

    if is_quadra and is_digit and is_unique and is_valid:
        return True

    return False


def create_hospital():
    hospital_name = input("Enter name: ")
    hospital_branch = input("Enter branch: ")
    hospital = Hospital(hospital_name, hospital_branch)
    return hospital


def create_doctor(hospital):


    while True:
        print("---------------------------")
        person_id = input("Enter ID (2XXX): ")

        if id_validator(hospital, person_id, "doctor"):
            break

    name = input("Enter name: ")
    gender = input("Enter gender: ")
    specialization = input("Enter specialization:")
    print("---------------------------")

    doctor = Doctor(person_id, name, gender, specialization)
    hospital.add_doctor(doctor)

    print("--> new doctor added...")
    print("---------------------------")

def create_patient(hospital):

    while True:
        print("---------------------------")
        person_id = input("Enter ID (4XXX): ")
        if id_validator(hospital, person_id, "patient"):
            break

    name = input("Enter name: ")
    age = input("Enter age: ")
    gender = input("Enter gender [M/F]: ")
    print("---------------------------")

    patient = Patient(person_id, name, age, gender)
    hospital.add_patient(patient)

    print("--> new patient added..")
    print("---------------------------")


def create_nurse(hospital):
    while True:
        print("---------------------------")
        person_id = input("Enter ID (3XXX): ")
        if id_validator(hospital, person_id, "nurse"):
            break

    name = input("Enter name: ")
    gender = input("Enter gender [M/F]: ")
    shift = input("Enter shift of nurse: ")
    print("---------------------------")

    nurse = Nurse(person_id, name, gender, shift)
    hospital.add_nurse(nurse)

    print("--> new nurse added..")
    print("---------------------------")


def display_doctor(hospital):
    hospital.display_doctors()

def display_patient(hospital):
    hospital.display_patients()

def display_nurse(hospital):
    hospital.display_nurses()
