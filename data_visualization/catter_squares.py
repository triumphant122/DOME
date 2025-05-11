import matplotlib
matplotlib.use('TkAgg') ## 指定后端
import matplotlib.pyplot as plt

x_values = [1,2,3,4,5]
y_values = [1,4,9,16,25]

plt.style.use('seaborn-v0_8')  ## 应用样式时，要单独的设置字体，否则会不显示中文
plt.rcParams['font.sans-serif'] = ['WenQuanYi Zen Hei']  ## 设置字体
fig,ax = plt.subplots()
# scatter传递两个列表
ax.scatter(x_values,y_values,s=100) # s代表点的尺寸

#设置标题和坐标轴名称
ax.set_title('平方数',fontsize=24)
ax.set_xlabel('值',fontsize=14)
ax.set_ylabel('值的平方',fontsize=14)

#设置刻度标记的大小
ax.tick_params(axis='both',which='major',labelsize=14)

plt.show()