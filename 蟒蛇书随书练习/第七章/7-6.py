#7-6.py
active =True
while active:
    age = input("please tell me your age \n")
    if age =='quit':
        break
    elif int(age)<=3:
        print ("\tyou are free!")
    elif int(age)>3 and int (age)<=12:
        print ("\tyou need to pay 10")
    elif int(age) >12:
        print("\t you need to pay 15")
