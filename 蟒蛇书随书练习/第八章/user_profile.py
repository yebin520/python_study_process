#user_profile.py
def buile_person(first,last,**user_info):
    user_info ['first']=first
    user_info ['last'] = last
    return user_info
user_profile = buile_person('Chen','Yebin',age='16',lacation='qz5z')
print (user_profile['age'])