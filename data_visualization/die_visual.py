from plotly.graph_objs import Bar,Layout
from plotly import offline

from die import Die
 # 创建1个D6和1个D10。
die_1 = Die()
die_2 = Die(10)
# 掷几次骰子并将结果储存在一个列表当中，
results = []
for roll_num in range(50_000):  ## 投掷100次骰子
    result = die_1.roll() + die_2.roll()  ## 将结果赋值给result
    results.append(result)  ## 将结果添加到results列表当中


## 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range (2,max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

## 对结果进行可视化
x_values = list(range(2,max_result+1))  ## x轴为可能出现的点，也就是从1-6,创建一个列表并且保存，list()函数可以将其他格式转换为列表
data = [Bar(x=x_values,y=frequencies)]  ## Bar()用来绘制条形图，Bar是一个类，这个类要放到中括号当中

x_axis_config = {'title':'结果','dtick':1}  ## dtick 键值对设置的是刻度
y_axis_config = {'title':'结果的频率'}
my_layout = Layout(title='掷一个D6和一个D10 50000次的结果',
                   xaxis=x_axis_config,yaxis=y_axis_config)
offline.plot({'data':data,'layout':my_layout},filename='d6_d10.html')