# Authentication System
from abc import ABC, abstractmethod

class AuthMethod(ABC):
    @abstractmethod
    def authenticate(self):
        pass

class PasswordAuth(AuthMethod):
    def authenticate(self):
        print("Authenticated using password.")

class OTPAuth(AuthMethod):
    def authenticate(self):
        print("Authenticated using OTP.")

auth = OTPAuth()
auth.authenticate()
