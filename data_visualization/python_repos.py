import requests

## Web API是网站的一部分，用于与使用特定的URL请求特定信息的程序进行交互，这种请求称为API调用

##下面代码会自动执行调用API并且处理返回结果。
# 执行API调用并储存响应
url='https://api.github.com/search/repositories?q=language:python&sort=stars' # 储存API调用的URL
headers = {'Accept':'application/vnd.github.v3+json'}  ##   headers可以显示的要求使用那个版本的API
r = requests.get(url,headers=headers)  # 使用requests调用API，调用get（）,并且将URL传递给它，然后再将相应的变量赋值给r
print(f"Status code:{r.status_code}")  # 这个API会返回JSON格式的信息

# 将API相应赋值给一个变量
response_dict = r.json() ## 因为API返回的是JSON格式的信息，因此使用json模块进行处理，将其返回一个字典
print(f"Total repositories:{response_dict['total_count']}")  ## 打印与total_count相关联的值，它指出了github总共有多少python库

# 探索有关仓库的信息
repo_dicts = response_dict['items']  ## items 关联的值是一个列表，嵌套了很多字典，每个字典都包含了一个关于python仓库的信息，将字典列表储存在变量当中
print(f"Repositories returned:{len(repo_dicts)}")

print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print(f"\nName: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Description: {repo_dict['description']}")

# 研究第一个仓库
#repo_dict = repo_dicts[0]  ## 提取之前字典列表的第一个字典

#print("\nSelected information about first repository:")
#print(f"Name:{repo_dict['name']}")  ## 项目名称
#print(f"Owner:{repo_dict['owner']['login']}")  ## 项目所有者
#print(f"Stars:{repo_dict['stargazers_count']}")  ## 多少收藏
#print(f"Repository:{repo_dict['html_url']}")  ## url地址
#print(f"Created: {repo_dict['created_at']}")  ## 创建时间
#print(f"Updated: {repo_dict['updated_at']}")  ## 更新时间
#print(f"Description: {repo_dict['description']}")  ## 描述

#print(f"\nKeys:{len(repo_dict)}") ##查看这个字典有多少键
#for key in sorted(repo_dict.keys()):  ## 打印这个字典的信息
   # print(key)

# 处理结果
#print(response_dict.keys())