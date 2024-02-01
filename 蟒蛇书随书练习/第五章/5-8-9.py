#5-8-9.py
customers = ['Yebin','admin','Yibin','Cj','Cl']
#customers = []
if customers:
    for customer in customers:
     if customer == 'admin' :
         print (f"Hello {customer},would you like to see a stasus report?")
     else:
         print (f"Hello {customer},thank you for you logging in again")
else :
    print ("We need to find some user!")