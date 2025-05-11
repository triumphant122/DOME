import json

# 探索数据的结构
filename = '/home/triumph_k/python_study/project/data_visualization/eq_data_1_day_m1.json'
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
print(mags[:10])
print(titles[:2])
print(lons[:5])
print(lats[:5])