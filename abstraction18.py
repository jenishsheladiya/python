# Logger System
from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass

class FileLogger(Logger):
    def log(self, message):
        print(f"Writing to file: {message}")

class ConsoleLogger(Logger):
    def log(self, message):
        print(f"Console: {message}")

logger = FileLogger()
logger.log("System started.")
