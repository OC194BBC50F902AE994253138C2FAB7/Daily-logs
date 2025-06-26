class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def display(self):
        print(f"Name: {self.name}, Breed: {self.breed}")

d = Dog("Buddy", "Golden Retriever")
d.display()

# --------------------------------------------
class Base:
    def __init__(self):
        self.value = 100

class Derived(Base):
    def __init__(self):
        super().__init__()
        print("Value from Base:", self.value)     # Correct

d = Derived()
