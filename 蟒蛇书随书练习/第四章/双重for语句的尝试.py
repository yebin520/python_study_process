#双重for语句的尝试.py
mapsx = []
mapsy = []
for x in range(1,11):
    mapsx.append(x)
    for y in range (1,11):
    	mapsy.append(y)
    	print (mapsx[x-1],mapsy[y-1],"\n")