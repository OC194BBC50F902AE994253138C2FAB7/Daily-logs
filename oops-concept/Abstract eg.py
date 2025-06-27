from abc import ABC,abstractmethod

class Flowers(ABC):
    @abstractmethod
    def smellsgood(self):
        pass

class lilly(Flowers):
    def smellsgood(self):
        return "WHITE LILLY "

class crocus(Flowers):
    def smellsgood(self):
        return "PURPLE CROCUS"
    
# obj1=lilly()
# print(obj1.smellsgood())

# obj2=crocus()
# print(obj2.smellsgood())


    