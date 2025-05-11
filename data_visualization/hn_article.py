import requests
import json

# 执行API调用并储存响应
url='https://hacker-news.firebaseio.com/v0/item/19155826.json'
r = requests.get(url)
print(f"Status code:{r.status_code}")

# 探索数据结构
response_dict = r.json()
readable_file = '/home/triumph_k/python_study/project/data_visualization/readable_hn_data.json'
with open(readable_file,'w') as f:
    json.dump(response_dict,f,indent=4)