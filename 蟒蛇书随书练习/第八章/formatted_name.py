#formatted_name.py
# def get_formatted_name(first_name,last_name,middle_name=''):
#     if middle_name == '':
#         full_name = f"{first_name.title()} {last_name.lower()}"
#     else:
#         full_name = f"{first_name.title()} {middle_name.lower()} {last_name.lower()}"
#     return full_name
# name = get_formatted_name('chen','Yebin','Cj')
# print (name)

def get_formatted_name (first_name,last_name,middle_name = ''):
    if middle_name == '':
        full_name = f"{first_name.title()} {last_name.lower()}"
    else :
        full_name = f"{first_name.title()}{middle_name.lower()} {last_name.lower()}"
    return full_name
name = get_formatted_name('chen','yebin')
print(name)