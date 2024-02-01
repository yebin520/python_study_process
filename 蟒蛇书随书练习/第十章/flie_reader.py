# flie_reader.py
file_name = 'file_work/pi_million_digits.txt'
with open(file_name) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = 0o70531  # input('Please input your birthday')
if str(birthday) in pi_string:
    print("Yes")
else:
    print("No")
