#cars.py
#.sort()的运用
cars = ['bmw','audi','toyota','subaru']
cars.sort();
print (cars)
cars.sort(reverse=True)
print (cars)
cars = ['bmw','audi','toyota','subaru']
print ("This is the original list:\t")
print (cars,"\n");
print ("This is the sorted list:\t")
print (sorted(cars),"\n");
print (cars)
print (sorted(cars,reverse=True))