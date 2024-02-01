#User.py
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

the_first_user = User("Chen","Yebin","16")
the_first_user.describe_user()
the_first_user.greet_user()

for i in range (1,5):
    the_first_user.increment_login_attempts()
print (the_first_user.login_attempts)
the_first_user.reset_login_attempts()
print (the_first_user.login_attempts)