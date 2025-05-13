# Database Connection Abstraction
from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

class MySQL(Database):
    def connect(self):
        print("Connected to MySQL Database.")

class PostgreSQL(Database):
    def connect(self):
        print("Connected to PostgreSQL Database.")

db = PostgreSQL()
db.connect()
