from datetime import datetime

class Patient:
    def __init__(self, name, age, diagnosis, contact):
        self.name = name
        self.age = age
        self.diagnosis = diagnosis
        self.contact = contact
        self.admission_time = datetime.now()

    def display(self):
        return f"{self.name} - {self.diagnosis}"