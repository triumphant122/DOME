import requests
from plotly.graph_objects import Bar
from plotly import offline

# 执行API调用并储存相应
url='https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': "application/vnd.github.v3+json"}
r = requests.get(url,headers=headers)
print(f"Status code:{r.status_code}")

# 处理结果
response_dict = r.json()
repo_dicts = response_dict['items']

## 当我们鼠标移动到条形时会显示信息，这个功能称为工具提示，现在我们要自定义工具提示
# repo_names,stars,labels = [],[],[]  ## 创建两个空列表，用来储存信息，一个是每个项目的名称，一个是获得的收藏数。
repo_links,stars,labels = [],[],[] 
for repo_dict in repo_dicts:  ## 遍历之前的提取出来内容
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    #repo_names.append(repo_dict['name'])  ## 将名字和收藏数添加到我们之前定义的列表当中。
    stars.append( repo_dict['stargazers_count'])
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}"
    labels.append(label)

# 可视化
data = [{  ## 定义了两个列表，当中嵌套了几个字典
    'type':'bar',
    'x':repo_links,
    'y':stars,
    'hovertext':labels,
    'marker':{
        'color':'rgb(60,100,150)',
        'line':{'width':1.5,'color':'rgb(25,25,25)'}
    },
    'opacity':0.6,
    }]
my_layout = {  ## 定义了字典定义图标的布局
    #'title':'GitHub上最受欢迎的python项目',就版本的语法，新版本无法使用，要修改
    #'titlefont':{'size':28},
    #'xaxis':{'title':"Repository"},
    'title':{
        'text':'GitHub中最受欢迎的Python项目',
        'font':{'size':28},
    },
    'xaxis':{
        'title':{
            'text':'Repository',
            'font':{'size':24},
        },
        'tickfont':{'size':14},
    },
    #'yaxis':{'title':'Stars'},
    'yaxis':{
        'title':{
            'text':'Stars',
            'font':{'size':24},
        },
        'tickfont':{'size':14},
    },
}
fig = {'data':data,'layout':my_layout}
offline.plot(fig,filename='python_repos4.html')