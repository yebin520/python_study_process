#4-6.py
numbers = [i for i in range(1,21,2)]
for i in range(0,len(numbers)):
	print(numbers[i])
number_first_3 = numbers[0:3]
number_last_3 = numbers[-3:]
a1 = int((len(numbers))/2-2)
a2 = int((len(numbers))/2+1)
number_middle_3 = numbers[a1:a2]
print (f"The first three itmes in this list are:{number_first_3}")
print (f"The middle three itmes in this list are:{number_middle_3}")
print (f"The last three itmes in this list are:{number_last_3}")