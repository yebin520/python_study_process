import matplotlib.pyplot as plt
values = [i for i in range(1,11)]
squares = [i**2 for i in range(1,11)]


plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.plot(values,squares,linewidth=3)

ax.set_title("平方数",fontsize=24)
ax.set_xlabel("数值",fontsize=20)
ax.set_ylabel("数值的平方",fontsize=20)
ax.tick_params(axis='both',labelsize=14)
plt.show()