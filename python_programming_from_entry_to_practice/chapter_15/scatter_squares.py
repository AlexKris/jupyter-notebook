import matplotlib.pyplot as plt

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, s=10)
# ax.scatter(x_values, y_values, c='red', s=10)
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# 设置图表标题并给坐标轴加上标签
ax.set_title("square", fontsize=24)
ax.set_xlabel("val", fontsize=14)
ax.set_ylabel("val^2", fontsize=14)

# 设置刻度标记的大小
# ax.tick_params(axis='both', which='major', labelsize=14)

# 设置每个坐标轴的取值范围
ax.axis([0, 1100, 0, 1100000])

# plt.show()

# 自动保存文件，第一个实参数为文件名，第二个参数将图表多余的空白区域剪裁掉
plt.savefig('squares_plot.png', bbox_inches='tight')