#8-13.py
def bulid_person(first,last,**user_info):
    user_info ['first'] = first
    user_info ['last']  = last
    return user_info
user_profile=bulid_person('Chen','yebin',
    age = '16',location = 'qz5z',
    fovarite_subject = 'math')
print (user_profile)