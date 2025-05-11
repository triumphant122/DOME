import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = '/home/triumph_k/python_study/project/data_visualization/sitka_weather_2018_simple.csv'  
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

# 从文件中获取降雨量数据
    prcps,dates = [],[]
    for row in reader:
        current_date = datetime.strptime(row[2],'%Y-%m-%d')
        try:
            prcp = float(row[3])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            prcps.append(prcp)

# 根据降雨量绘制图形
plt.style.use('seaborn-v0_8')
plt.rcParams['font.sans-serif'] = ['WenQuanYi Zen Hei']  ## 设置字体
fig,ax = plt.subplots()  ## subplots函数时用来创建一个图片和一个或多个坐标轴
ax.plot(dates,prcps,c='red')

# 设置图片的格式
ax.set_title("2018年每日降雨量",fontsize=24)
ax.set_xlabel('',fontsize=16)
ax.set_ylabel("降雨量(mm)",fontsize=16)
ax.tick_params(axis='both',which='major',labelsize=16)
plt.show()
