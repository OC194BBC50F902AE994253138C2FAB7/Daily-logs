#PUBLIC ACCESS MODIFIER

class Public:
    def __init__(self):
        self.name = 'Aruna' 

    def display(self):
        print(self.name)

obj =  Public() 
obj.display() # or 
#print(obj.name)--------------------------

# #PROTECTED ACCESS MODIFIER 

class Protected:
    def __init__(self):
        self._age = 19
class Subclass(Protected):
    def Age(self):
        print(self._age)

obj1 =  Subclass()
obj1.Age()

#PRIVATE ACCESS MODIFIER

class Private:
    def __init__(self):
        self.__place = 'West Tambaram'
    def pvt(self):
        print(self.__place)

obj2 =  Private()
obj2.pvt()



    










        

        
