file_path = 'learning_python.txt'
with open(file_path) as file_object :
    contents = file_object.read()
    file_object.seek(0)
    lines = file_object.readlines()
print (contents.strip())
print ("-----------")
for line in lines :
    print (line.strip())
