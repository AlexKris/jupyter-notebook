from die import Die
from plotly.graph_objs import bar, Layout
from plotly import offline

# 创建一个D6
die = Die()

# 掷几次骰子并将结果存储在一个列表中
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

# 分析结果
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# print(frequencies)

# 对结果进行可视化
x_values = list(range(1, die.num_sides+1))
data = [bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'result'}
y_axis_config = {'title': 'freq of result'}
my_layout = Layout(title="throw D6 1000 times's result", xaxis = x_axis_config, yaxis = y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')