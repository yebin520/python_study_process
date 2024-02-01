#admin.py
class User:
    """docstring for User"""
    def __init__(self, first_name,last_name,age):
        self.first_name = first_name
        self.last_name =last_name
        self.age = age 
        self.full_name = f"{first_name} {last_name}"
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts (self):
        self.login_attempts = 0
    def greet_user (self):
        print (f"Hello {self.full_name.title()}")
    def describe_user(self):
        print (f"The user's name is {self.full_name.title()} and his name is {self.age}")

class Privileges:
    """docstring for privileges"""
    def __init__(self, privileges = ['can add post','can delet post','can ban user']):
        self.privileges = privileges
    def show_privileges (self):
        print (self.privileges)

class Admin(User):
    """docstring for Admin"""
    def __init__(self, first_name,last_name,age):
        super().__init__(first_name,last_name,age)
        #self.privileges = ['can add post','can delet post','can ban user']
        self.privileges = Privileges()
        