from profile import Profile

class UserData:
    def __init__(self, name, age, email, phn):
        self.name = name
        self.age = age
        self.email = email
        self.phn = phn

    def show_data(self):
        print( "USER INFO! ")
        
        return f"name: {self.name}, age: {self.age},email: {self.email},phn: {self.phn}"

ME = UserData('Aruna', 19, 'a@gmail.com', 7010835313)
FRND = UserData('kee', 20, 'k@gmail.com',7904340629)

print(FRND.show_data())































