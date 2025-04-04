import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.style.use('seaborn')
# 在一张图片中绘制一个或多个图表，fig表示整张图片，ax表示图片中的各个图表
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)# linewidth设置线条粗细

# 设置图表标题并给坐标轴加上标签
ax.set_title("square", fontsize=24)
ax.set_xlabel("val", fontsize=14)
ax.set_ylabel("val^2", fontsize=14)

# 设置刻度标记的大小
ax.tick_params(axis='both', labelsize=14)

plt.show()