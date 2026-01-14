from main import Patient, Doctor, Appointment 


patient1 = Patient("Laylo", 34)
patient2 = Patient("Ali", 28)

doctor1 = Doctor("Dr. Azizov", "Kardiolog")
doctor2 = Doctor("Dr. Karimova", "Nevrolog")

appointment1 = Appointment("2025-05-23", patient1, doctor1)
appointment2 = Appointment("2025-05-24", patient2, doctor2)

appointment1.show_appointment()
appointment2.show_appointment()
