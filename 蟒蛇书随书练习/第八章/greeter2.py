#greeter2.py
def get_formmated_name(first_name,last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()
while True:
    f_name = input("\nPlease tell me your first name is:")
    l_name = input("\nPlease tell me your last name is:")
    name = get_formmated_name(f_name,l_name)
    print ("\n\tYour full name is :",name)