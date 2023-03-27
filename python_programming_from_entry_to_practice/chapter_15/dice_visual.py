from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

# 创建一个D6和一个D10
die_1 = Die()
die_2 = Die(10)

# 掷几次骰子并将结果存储在一个列表中
results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# print(frequencies)

# 对结果进行可视化
x_values = list(range(1, max_result+1)) # 将可能出现的点数存储
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'result', 'dtick': 1} # dtick x轴显示的刻度间距
y_axis_config = {'title': 'freq of result'}
my_layout = Layout(title="throw D6 1000 times's result", xaxis = x_axis_config, yaxis = y_axis_config)

# 生成图表
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10.html')