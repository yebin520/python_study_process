#5-11.py
numbers = [i for i in range (1,10)]
for i in range (9):
    if(numbers[i]==1):
        print ("1st")
    elif (numbers[i]==2):
        print ("2nd")
    elif (numbers[i]==3):
        print("3rd")
    else:
        print (f"{numbers[i]}th")