from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Bike(Vehicle):
    def start_engine(self):
        return "ENGINE STARTED"
    
class Car(Vehicle):
    def start_engine(self):
        return"ENGINE STARTED"
    
a=Bike()
a.start_engine()
print(a.start_engine())

b=Car()
b.start_engine()
print(b.start_engine())


    