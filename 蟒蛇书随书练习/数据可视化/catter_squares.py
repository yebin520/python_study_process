import matplotlib.pyplot as plt

x_values = [i for i in range(1, 1001)]
y_values = [i ** 2 for i in range(1, 1001)]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values,c=y_values,cmap=plt.cm.Blues, s=10)

ax.set_title("Square numbers", fontsize=24)
ax.set_xlabel("numbers", fontsize=14)
ax.set_ylabel("Square numbers", fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=14)
ax.axis([0, 1000, 0, 1100000])
plt.savefig('Squares_plot.png',bbox_inches='tight')
#plt.show()
