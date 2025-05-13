# Notification System
from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

class Email(Notification):
    def send(self, message):
        print(f"Sending email: {message}")

class SMS(Notification):
    def send(self, message):
        print(f"Sending SMS: {message}")

n = Email()
n.send("Meeting at 3 PM.")
