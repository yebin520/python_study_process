#range和list的运用.py
numbers = list (range (1,11,2))
print (numbers)

# squares = list(range(1,11))
# for i in range(0,10):
# 	squares[i]=squares[i]*squares[i];
# print (squares)



# squares = []
# for i in range (1,11):
# 	squares.append(i**2)
# print (squares)

squares = [value**2 for value in range(1,11)]
print (squares)