import plotly.express as px
import json
import pandas as pd



# 探索数据的结构
filename = '/home/triumph_k/python_study/project/data_visualization/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)   ## 载入上述数据，帮将其赋值给变量

#readable_file = '/home/triumph_k/python_study/project/data_visualization/readable_eq_data.json'
#with open(readable_file,'w') as f:
#    json.dump(all_eq_data,f,indent=4) # 设置缩进量，加载数据

all_eq_dicts = all_eq_data['features']  ## 提取与'features'键相关的数据并且赋值给变量
# 提取震级、位置数据
mags,titles,lons,lats = [],[],[],[]
for eq_dict in all_eq_dicts:  # 遍历数据
    mag = eq_dict['properties']['mag']
    title = eq_dict['properties']['title']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)

# 另一种指定数据的方式
data = pd.DataFrame(
    data=zip(lons,lats,titles,mags),columns=["经度","纬度","位置","震级"]
)
data.head()

# 绘制地震散点图
## 教材上的内容有点老
fig = px.scatter_geo(  ## 原来代码为px.scatter
    data,
    lon="经度",
    lat="纬度",
    #lon=lons, # 原来为x=lons
    #lat=lats, # 原来为y=lats
    labels={"lon":"经度","lat":"纬度"},
    projection='natural earth',
    scope='world', # 这是新加的一行代码
    # range_x=[-180,180], 这是原来的两行代码
    # range_y=[-90,90],
    width=800,
    height=800,
    title="全球地震散点图",
    size="震级",
    size_max=10,
    color="震级",
    hover_name="位置",
    )
fig.write_html("global_earthquakes3.html")
fig.show()