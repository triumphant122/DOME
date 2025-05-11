## 读取csv文件要使用到csv模块，读取json要用到json模块
## csv文件就是以逗号为分隔符的值，存储在文本文件当中
## 例如
## "USW00025333","SITKA AIRPORT, AK US","2018-01-01","0.45",,"48","38"
## 上述含义是阿拉斯加州锡特卡2018年1月1日的天气数据，有最高温度和最低温度。
## csv数据，人阅读起来非常麻烦，但是机器可以很快的提取
import csv
import matplotlib.pyplot as plt
from datetime import datetime


filename = '/home/triumph_k/python_study/project/data_visualization/sitka_weather_2018_simple.csv'  
## 将要使用的文件的名称赋值给filename。
with open(filename) as f:  ## 打开这个文件并将这个文件赋值给f
    reader = csv.reader(f)  ## 使用csv.reader()函数创建一个与该文件相关联的阅读器对象，将前面储存的文件对象f作为实参传递给函数，最好赋值给reader
    header_row = next(reader)  ## 调用next()函数，并将之前的阅读器对象传递给他,它将返回文件中的下一行，最后赋值给header_row

    # 从文件中获取日期最高温度、最低温度
    dates,highs,lows = [],[],[]  ## 创建两个空列表，分别用来储存日期和最高温度、最低温度
    for row in reader:   ## for循环遍历刚创建的阅读器对象
        current_date = datetime.strptime(row[2],'%Y-%m-%d')  ## 将row中的第一列进行切片取出并且赋值给变量。
        high = int(row[5])  ## row中的第五例进行切片，然后将每一个值都进行转换成整数操作，赋值给high
        low = int(row[6])
        dates.append(current_date)  ## 将切片出来的值添加到先前创建的空列表当中
        highs.append(high) ## 使用append函数将每个循环的值添加到highs列表当中
        lows.append(low)
# print(highs)

# 根据最高温度绘制图形
plt.style.use('seaborn-v0_8')
plt.rcParams['font.sans-serif'] = ['WenQuanYi Zen Hei']  ## 设置字体
fig,ax = plt.subplots()
ax.plot(dates,highs,c='red')
ax.plot(dates,lows,c='blue')
ax.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1) ## 其中alpha为透明值

# 设置图形格式
ax.set_title("2018年每日最高温度",fontsize=24)
ax.set_xlabel('',fontsize=16)
ax.set_ylabel("温度(F)",fontsize=16)
ax.tick_params(axis='both',which='major',labelsize=16)

plt.show()

 ## 将文件头以及位置打印出来
    #for index,column_header in enumerate(header_row):  ## enumerate()函数可以获取每个元素的索引及其值
       # print(index,column_header)



 
    ## 上述文件中next()只调用了一次，因此此时会显示文件的第一行

