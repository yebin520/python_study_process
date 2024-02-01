import json
filename = 'file_work/username.json'
def get_stored_username():
    try:
        with open(filename) as f:
            names = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return names

def get_new_name():
    username = input("What is your name?")
    with open(filename, 'w') as f:
        json.dump(usernames, f)
def greet_user():
    username = get_stored_username()
    if username:
        print (username)
    else :
        get_new_name()
greet_user()