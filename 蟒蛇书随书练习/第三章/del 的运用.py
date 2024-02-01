#del 的运用.py
#使用del删除列表中的某一个元素
motorcycles =[];
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print (motorcycles)

motorcycles.insert(1,'ducati')
print (motorcycles);

del motorcycles[1]
print (motorcycles)