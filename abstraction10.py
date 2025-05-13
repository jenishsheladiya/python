# Remote Control Devices
from abc import ABC, abstractmethod

class RemoteControl(ABC):
    @abstractmethod
    def turn_on(self):
        pass

class TV(RemoteControl):
    def turn_on(self):
        print("Turning on the TV.")

class AC(RemoteControl):
    def turn_on(self):
        print("Turning on the Air Conditioner.")

device = AC()
device.turn_on()
