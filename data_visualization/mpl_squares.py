import matplotlib
matplotlib.use('TkAgg') ## 指定后端
import matplotlib.pyplot as plt

input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]

plt.style.use('seaborn-v0_8')  ## 应用样式时，要单独的设置字体，否则会不显示中文
plt.rcParams['font.sans-serif'] = ['WenQuanYi Zen Hei']  ## 设置字体
fig,ax = plt.subplots()  ## 调用subplots函数，fig表示整个图，ax表示每个图标
ax.plot(input_values,squares,linewidth=3)  ## linewidth设置线条粗细

# 设置图标标题，给坐标轴加上标签
ax.set_title('平方数',fontsize=24)  ## 指定标题
ax.set_xlabel('值',fontsize=14)
ax.set_ylabel('值的平方',fontsize=14)
# 设置刻度标记的大小
ax.tick_params(axis='both',labelsize=14)  ## axis指定刻度
plt.show()

## 教材中使用的代码在VScode中出现报错，显示使用非交互式后端
## 要不指定使用某个交互式后端，要不就不在窗口进行显示，直接将结果保持为图片
## 新知识，交互式后端

## 解决方案1
## 首先安装jupyter依赖库
## 在设置当中Theme Matplotlib Plots 勾选
## 右键点击文件在交互式窗口执行该文件

## 解决方案2
## 在使用sudo apt-get install python3-tk代码安装TkAgg后端，并且设置指定后端后问题解决

## 不显示中文问题
## 可以在代码中导入matplotlib.pyplot后，直接指定支持中文的字体，示例如下:
#import matplotlib.pyplot as plt

# 设置中文字体
#plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows系统常用字体
# plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 微软雅黑
# plt.rcParams['font.sans-serif'] = ['WenQuanYi Zen Hei']  # Linux系统常用字体
# plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # macOS系统常用字体

# 解决负号显示问题
#plt.rcParams['axes.unicode_minus'] = False

# 绘图测试
#plt.plot([1, 2, 3], [4, 5, 6])
#plt.title('中文标题')  # 应正常显示中文
#plt.show()

## 另一个解决方案是安装中文字体包：sudo apt-get install fonts-wqy-zenhei  # Ubuntu/Debian
## import matplotlib
## print(matplotlib.matplotlib_fname())  # 输出配置文件路径（如`/path/to/matplotlibrc`）  查找到这个文件后修改配置文件
#  font.family         : sans-serif
#  font.sans-serif     : SimHei, Microsoft YaHei, WenQuanYi Zen Hei, DejaVu Sans, ...  # 添加中文字体到列表开头
#  axes.unicode_minus  : False  # 解决负号显示问题
## 对上述文件进行修改后，执行rm -rf ~/.cache/matplotlib 重启即可生效

# 默认配置文件是模板：Matplotlib安装目录下的matplotlibrc（如site-packages/matplotlib/mpl-data/matplotlibrc）是只读模板，用户应编辑自己目录下的配置文件。
# 手动添加设置：如果用户目录下的配置文件中没有相关配置，直接添加上述内容即可