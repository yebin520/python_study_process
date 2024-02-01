#if的运用.py
name = 'YIBIN'
if name.lower() == 'yibin' :
    print ("I like you!")
num_1 = 21;num_2 =39
if (num_1==21) and (num_2==39):
    print (num_1+num_2)
if (num_1 == 21) or (num_2 ==21):
    print (num_1 +num_2 )

car ='subway'
print (car == 'subway')

cars = ['subway','train','bus','plane']
if car not in cars:
    print ('Right')
else:
    print ('Wrong')