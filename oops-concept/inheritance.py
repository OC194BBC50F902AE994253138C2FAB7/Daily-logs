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

#Multiple inheritance

class Mother :
    def mother(self, mothername):
        print(self.mothername)


class Father:
    def father(self,fathername):
        print(self.fathername)

class Child(Mother, Father):
    def parents(self):
        print("MOTHER:",self.mothername)
        print("FATHER:",self.fathername)
    
a = Child()
a.fathername = "k"
a.mothername ="A"
a.parents()
#---------------------------------------------------------------------------
# multilevel inheritance
# Base class
class Grandfather:

    def __init__(self, grandfathername):
        self.grandfathername = grandfathername

# Intermediate class
class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername

        # invoking constructor of Grandfather class
        Grandfather.__init__(self, grandfathername)

# Derived class
class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname

        # invoking constructor of Father class
        Father.__init__(self, fathername, grandfathername)

    def print_name(self):
        print('Grandfather name :', self.grandfathername)
        print("Father name :", self.fathername)
        print("Son name :", self.sonname)


#  Driver code
s1 = Son('Shanmugam', 'K', 'Rakul')
print(s1.grandfathername)
s1.print_name()

# ---------------------------------------------------------

# Hierarchical inheritance
# Base class
class Parent:
    def func1(self):
        print("This function is in parent class.")

# Derived class1
class Child1(Parent):
    def func2(self):
        print("This function is in child 1.")

# Derivied class2
class Child2(Parent):
    def func3(self):
        print("This function is in child 2.")
# Driver's code
object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()

# -------------------------------------------------------------
# hybrid inheritance

class School:
    def func1(self):
        print("This function is in school.")

class Student1(School):
    def func2(self):
        print("This function is in student 1. ")

class Student2(School):
    def func3(self):
        print("This function is in student 2.")

class Student3(Student1, School):
    def func4(self):
        print("This function is in student 3.")

# Driver's code
object = Student3()
object.func1()
object.func2()

#---------------------------------------------------























    