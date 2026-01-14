class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age

class Doctor:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty

class Appointment:
    def __init__(self, date, patient, doctor):
        self.date = date
        self.patient = patient
        self.doctor = doctor

    def show_appointment(self):
        print(f"Sana: {self.date}")
        print(f"Bemor: {self.patient.name}, {self.patient.age} yosh")
        print(f"Shifokor: {self.doctor.name}, {self.doctor.specialty}")
        print()
