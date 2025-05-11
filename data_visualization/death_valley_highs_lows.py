import csv
import matplotlib.pyplot as plt
from datetime import datetime


filename = '/home/triumph_k/python_study/project/data_visualization/death_valley_2018_simple.csv'  
## 将要使用的文件的名称赋值给filename。
with open(filename) as f:  ## 打开这个文件并将这个文件赋值给f
    reader = csv.reader(f)  ## 使用csv.reader()函数创建一个与该文件相关联的阅读器对象，将前面储存的文件对象f作为实参传递给函数，最好赋值给reader
    header_row = next(reader)  ## 调用next()函数，并将之前的阅读器对象传递给他,它将返回文件中的下一行，最后赋值给header_row
    
    ## 编写代码，查看这个数据文件包含的文件头

    #for index,column_header in enumerate(header_row):
        #print(index,column_header)
    
    # 从文件中获取日期、最高温度和最低温度。
    dates,highs,lows = [],[],[]
    for row in reader:
        current_date = datetime.strptime(row[2],'%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high) ## 使用append函数将每个循环的值添加到highs列表当中
            lows.append(low)

# 根据最高温度绘制图形
plt.style.use('seaborn-v0_8')
plt.rcParams['font.sans-serif'] = ['WenQuanYi Zen Hei']  ## 设置字体
fig,ax = plt.subplots()
ax.plot(dates,highs,c='red')
ax.plot(dates,lows,c='blue')
ax.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1) ## 其中alpha为透明值

# 设置图形格式
title = "2018年每日最高温度和最低温度\n美国加利福尼亚州死亡谷"
ax.set_title(title,fontsize=20)
ax.set_xlabel('',fontsize=16)
ax.set_ylabel("温度(F)",fontsize=16)
ax.tick_params(axis='both',which='major',labelsize=16)

plt.show()