
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
        for doctor in self.doctors:
            doctor.display()

    def display_patients(self):
        for patient in self.patients:
            patient.display()

    def display_nurses(self):
        for nurse in self.nurses:
            nurse.display()

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

class Doctor(Person):
    def __init__(self, person_id, name, gender, specialization):
        super().__init__(person_id, name, gender)
        self.specialization = specialization

    def display(self):
        print("----------------------")
        super().display()
        print(f"Specialization: {self.specialization}")
        print("----------------------")



class Nurse(Person):
    def __init__(self, person_id, name, gender, shift):
       super().__init__(person_id, name, gender)
       self.shift = shift

    def display(self):
        print("----------------------")
        super().display()
        print(f"Specialization: {self.shift}")
        print("----------------------")


class Patient(Person):
    def __init__(self, person_id, name, age, gender):
        super().__init__(person_id, name, gender, age)

    def display(self):
        print("----------------------")
        super().display()
        print(f"Specialization: {self.age}")
        print("----------------------")
