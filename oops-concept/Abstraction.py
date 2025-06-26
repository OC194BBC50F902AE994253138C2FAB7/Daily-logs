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
    
# objs = [Bike(), Car()]
# for obj in objs:  
# print (obj.start_engine()) 

def obj_behaviour(objectName):
     return objectName.start_engine()

b= Bike()
c=Car()

print(obj_behaviour(Bike()))
print(obj_behaviour(Car()))