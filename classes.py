
class Hospital:
    def __init__(self, name, branch):
        self.name = name
        self.branch = branch
        self.doctors = []
        self.patients = []
        self.nurses = []

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def add_patient(self, patient):
        self.patients.append(patient)

    def add_nurse(self, nurse):
        self.nurses.append(nurse)

    def display_doctors(self):
        if self.doctors:
            for doctor in self.doctors:
                doctor.display()
        else:
            print("No doctors are currently registered.")

    def display_patients(self):
        if self.patients:
            for patient in self.patients:
                patient.display()
        else:
            print("No patients are currently registered.")

    def display_nurses(self):
        if self.nurses:
            for nurse in self.nurses:
                nurse.display()
        else:
            print("No nurses are currently registered.")

    def has_id(self, person_id, person):

        id_found = False
        person_object = None

        match person:
            case "doctor":
                for doctor in self.doctors:
                    id_found = doctor.has_id(person_id)
                    if id_found:
                        person_object = doctor
                        break
            case "nurse":
                for nurse in self.nurses:
                    id_found = nurse.has_id(person_id)
                    if id_found:
                        person_object = nurse
                        break
            case "patient":
                for patient in self.patients:
                    id_found = patient.has_id(person_id)
                    if id_found:
                        person_object = patient
                        break
        return id_found, person_object

    def remove_person(self, person_id, person):
        id_found, person_object = self.has_id(person_id, person)
        if id_found:
            print("successfully removed: ")
            person_object.display()
            match person:
                case "doctor":
                    self.doctors.remove(person_object)
                case "patient":
                    self.patients.remove(person_object)
                case "nurse":
                    self.nurses.remove(person_object)



class Person:
    def __init__(self, person_id, name, gender, age=None):
        self.person_id = person_id
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        print(f"ID: {self.person_id}")
        print(f"Name: {self.name}")
        print(f"Gender: {self.gender}")

    def has_id(self, person_id):
        if self.person_id == person_id:
            return True
        return False

    def update_name(self, name):
        self.name = name

    def update_gender(self, gender):
        self.gender = gender

    def update_age(self, age):
        self.age = age

class Doctor(Person):
    def __init__(self, person_id, name, gender, specialization):
        super().__init__(person_id, name, gender)
        self.specialization = specialization

    def display(self):
        print("----------------------")
        super().display()
        print(f"Specialization: {self.specialization}")
        print("----------------------")

    def update_specialization(self, specialization):
        self.specialization = specialization


class Nurse(Person):
    def __init__(self, person_id, name, gender, shift):
       super().__init__(person_id, name, gender)
       self.shift = shift

    def display(self):
        print("----------------------")
        super().display()
        print(f"Shift: {self.shift}")
        print("----------------------")

    def update_shift(self, shift):
        self.shift = shift



class Patient(Person):
    def __init__(self, person_id, name, age, gender):
        super().__init__(person_id, name, gender, age)

    def display(self):
        print("----------------------")
        super().display()
        print(f"Age: {self.age}")
        print("----------------------")
