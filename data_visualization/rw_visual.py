import matplotlib.pyplot as plt
from random_walk import RandomWalk

# 只要程序处于活动状态，就不断的模拟随机漫步

while True:
    # 创建一个RandomWalk实例。
    rw = RandomWalk()
    rw.fill_walk()
    # 将所有点都绘制出来
    plt.style.use('classic')
    fig,ax = plt.subplots()
    point_numbers = range(rw.num_points)  ## 使用range()生成了一个数字列表，其中包含的数与漫步的点数相同。
    #ax.scatter(rw.x_values,rw.y_values,c=point_numbers, cmap=plt.cm.Blues,
               #edgecolors='none',s=15)  ## 将参数c设置为之前range的列表，设置点的边缘为无色
    ax.plot(rw.x_values,rw.y_values,color = 'blue',linewidth=0.5)  ## 将参数c设置为之前range的列表，设置点的边缘为无色
    
    # 突出起点和终点
    #ax.scatter(0,0,c='green',edgecolors = 'none',s=100)  ## scatter是绘制散点图的函数,起点坐标设置为绿色
    #ax.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100) ## 终点坐标设置为红色
     # 突出起点和终点
    ax.scatter(0,0,c='green',edgecolors = 'none',s=100)  ## scatter是绘制散点图的函数,起点坐标设置为绿色
    ax.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100) ## 终点坐标设置为红色

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break

## 模拟多长随机漫步，将上述代码设置到一个while循环当中