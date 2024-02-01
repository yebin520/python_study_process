#练习4-2动物.py
animals = ['cat','dog','pig']
for animal in animals :
	print (f"A {animal} would make a great pet ")
print ("Any of these animals would make a great pet")
friends_animals = animals[:]
animals.append('fox')
friends_animals.append('rabbit')
print(animals)
print(friends_animals)