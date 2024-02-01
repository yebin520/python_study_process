User_name = input("Please write your name")
filename = 'file_work/10-3.txt'
with open(filename,'w') as file_object:
    file_object.write(User_name)