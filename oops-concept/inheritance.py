# single inheritance

# Base class
class Parent:
    def func1(self):
        print("PARENT CLASS.")

# Derived class
class Child(Parent):
    def func2(self):
        print("CHILD CLASS")

object = Child()
object.func1()
object.func2()