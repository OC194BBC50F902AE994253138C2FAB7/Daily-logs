# # single inheritance

# # Base class
# class Parent:
#     def func1(self):
#         print("PARENT CLASS.")

# # Derived class
# class Child(Parent):
#     def func2(self):
#         print("CHILD CLASS")

# object = Child()
# object.func1()
# object.func2()

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






















    