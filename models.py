# This file contains the main classes for clinic Queue Manager
from datetime import datetime

class Patient:
    def __init__(self, name):
        self.name = name
        self.time_added = datetime.now()

    def get_details(self):
        return f"{self.name} (Added at {self.time_added.strftime('%H:%M:%S')})"


class ClinicQueue:
    def __init__(self):
        self.queue = []
        self.served = 0

    def add_patient(self, patient):
        self.queue.append(patient)

    def serve_patient(self):
        if self.queue:
            self.served += 1
            return self.queue.pop(0)  # FIFO
        return None

    def get_all_patients(self):
        return self.queue

    def total_served(self):
        return self.served
