file_path = 'file_work/pi_million_digits.txt'
with open(file_path) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines :
    #print (line.rstrip())
    pi_string += line.strip()
birthday = input("请输入你的生日")
if birthday in pi_string:
    print ("Yes")
else:
    print ("No")
print (pi_string[:52])
print (len(pi_string))