from classes import Hospital, Doctor, Patient, Nurse

def id_validator(hospital, person_id, person):
    is_quadra = False
    is_digit = False
    is_available = False
    is_valid = False
    dict_id = {"doctor": '2', "nurse": '3', "patient": '4'}

    if not person_id.isdigit():
        print("ID must be in digits")
        return is_digit,None
    is_digit = True

    if not len(person_id) == 4:
        print("ID length must be equal to 4")
        return is_quadra,None
    is_quadra = True

    if not person_id[0] in list(dict_id.values()) or not person_id[0] == dict_id.get(person):
        print(f"{person} ID must start with {dict_id.get(person)}")
        return is_valid,None

    is_valid = True

    has_id, person_object = hospital.has_id(person_id, person)

    if not has_id:
        print("ID not found")
        return is_available,None
    is_available = True


    if is_quadra and is_digit and is_available and is_valid:
        return True,person_object

    return False


def id_validator_creation(hospital, person_id, person):
    is_quadra = False
    is_digit = False
    is_unique = False
    is_valid = False

    dict_id = {"doctor": '2', "nurse": '3', "patient": '4'}

    if not person_id.isdigit():
        print("ID must be in digits")
        return is_digit
    is_digit = True

    if not len(person_id) == 4:
        print("ID length must be equal to 4")
        return is_quadra
    is_quadra = True

    if not person_id[0] in list(dict_id.values()) or not person_id[0] == dict_id.get(person):
        print(f"{person} ID must start with {dict_id.get(person)}")
        return is_valid

    is_valid = True

    has_id, person_object =  hospital.has_id(person_id, person)

    if has_id:
        print("ID must be unique")
        return is_unique
    is_unique = True

    if is_quadra and is_digit and is_unique and is_valid:
        return True

    return False


def create_hospital():
    while True:
        hospital_name = input("Enter name: ")
        if is_valid_name(hospital_name):
            break
    while True:
        hospital_branch = input("Enter branch: ")
        if is_valid_name(hospital_branch):
            break

    hospital = Hospital(hospital_name, hospital_branch)
    return hospital


def create_doctor(hospital):


    while True:
        print("---------------------------")
        person_id = input("Enter ID (2XXX): ")

        if id_validator_creation(hospital, person_id, "doctor"):
            break

    while True:
        name = input("Enter name: ")
        if is_valid_name(name):
            break

    while True:
        gender = input("Enter gender: ").lower()
        if gender_validator(gender):
            break

    while True:
        specialization = input("Enter specialization:")
        if is_valid_name(specialization):
            break

    print("---------------------------")

    doctor = Doctor(person_id, name, gender, specialization)
    hospital.add_doctor(doctor)

    print("--> new doctor added...")
    print("---------------------------")

def create_patient(hospital):

    while True:
        print("---------------------------")
        person_id = input("Enter ID (4XXX): ")
        if id_validator_creation(hospital, person_id, "patient"):
            break

    while True:
        name = input("Enter name: ")
        if is_valid_name(name):
            break

    while True:
        age = input("Enter age: ")
        if age_validator(age):
            break

    while True:
        gender = input("Enter gender: ").lower()
        if gender_validator(gender):
            break
    print("---------------------------")

    patient = Patient(person_id, name, age, gender)
    hospital.add_patient(patient)

    print("--> new patient added..")
    print("---------------------------")


def create_nurse(hospital):
    while True:
        print("---------------------------")
        person_id = input("Enter ID (3XXX): ")
        if id_validator_creation(hospital, person_id, "nurse"):
            break

    while True:
        name = input("Enter name: ")
        if is_valid_name(name):
            break

    while True:
        gender = input("Enter gender: ").lower()
        if gender_validator(gender):
            break

    while True:
        shift = input("Enter shift of nurse: ")
        if is_valid_name(shift):
            break
    print("---------------------------")

    nurse = Nurse(person_id, name, gender, shift)
    hospital.add_nurse(nurse)

    print("--> new nurse added..")
    print("---------------------------")


def display_person(hospital, person):
    match person:
        case "doctor":
            hospital.display_doctors()
        case "patient":
            hospital.display_patients()
        case "nurse":
            hospital.display_nurses()


def search_by_id(hospital, person_id, person):
    is_available, person_object = id_validator(hospital, person_id, person)
    return is_available, person_object

def remove_person(hospital, person_id, person):
    hospital.remove_person(person_id, person)


def age_validator(age):
    if age.isdigit() and 0<int(age)<110:
        return True
    print("Invalid age...")
    return False

def is_valid_name(name):

    if len(name)<1 or name.isspace():
        print("Must not be empty!")
        return False

    for word in name.split():
        if not word.isalpha():
            print("Must be alphabetic")
            return False

    return True


def gender_validator(gender):
    if gender in {'m', 'f', 'male', 'female', 'others'}:
        return True
    print("Invalid gender...")
    return False
