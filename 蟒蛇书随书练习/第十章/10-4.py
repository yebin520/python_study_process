filename = 'file_work/10-4.txt'
""""enter 'Quit' to close the proceeding"""
while True:
    User_name = input("Please write your name")
    if User_name == 'Quit':
        print ("Over!!!")
        break
    with open(filename,'a') as file_object:
        User_name += '\n'
        file_object.write(User_name)