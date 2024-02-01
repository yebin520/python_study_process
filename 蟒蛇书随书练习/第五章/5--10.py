#5--10.py
low_users = []
current_users= ['Yebin','Yibin',"Yebin666",'Yebin6669',"Chenjing"]
new_users = ['hsy','Yibin','YEBIN666','CHENjng',"CHENLING"]
for i in range (len(current_users)):
    low_users.append(current_users[i].lower())
    if(low_users[i]==new_users[i].lower()):
        print ("The name has been used")
    else:
        print ("The name hasn't been used")