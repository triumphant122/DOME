import matplotlib
matplotlib.use('TkAgg') ## 指定后端
import matplotlib.pyplot as plt

x_values = range(1,1001)
y_values = [x**2 for x in x_values] # 从x_values列表当中遍历x值并计算x值的平方，并存储在y_values列表当中

plt.style.use('seaborn-v0_8')  ## 应用样式时，要单独的设置字体，否则会不显示中文
plt.rcParams['font.sans-serif'] = ['WenQuanYi Zen Hei']  ## 设置字体
fig,ax = plt.subplots()
# scatter传递两个列表
ax.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,s=10) # s代表点的尺寸

#设置标题和坐标轴名称
ax.set_title('平方数',fontsize=24)
ax.set_xlabel('值',fontsize=14)
ax.set_ylabel('值的平方',fontsize=14)

#设置刻度标记的大小
ax.tick_params(axis='both',which='major',labelsize=14)

#设置每个坐标轴的取值范围
ax.axis([0,1100,0,1100000]) ## 提供的4个值分别为x和y轴的最大值和最小值

plt.show()