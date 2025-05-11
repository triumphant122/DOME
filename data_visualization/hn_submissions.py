from operator import itemgetter
import requests

# 执行API调用并储存响应结果
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)  ## 使用requests.get调用这个url的API然后将结果储存到r变量当中
print(f"Status code:{r.status_code}")

# 处理有关每篇文章的信息
submission_ids = r.json()  # 使用json包进行加载，赋值给变量
submission_dicts = []  ## 创建一个空的列表
for submission_id in submission_ids[:30]:  ## 创建for循环进行调用API并且加载信息
    # 对每一篇文章都执行一个API调用。
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id:{submission_id}\tstatus:{r.status_code}")
    response_dict = r.json()

    # 对于每篇文章，都创建一个字典。

    ## 原文中的方法会出现错误，导致结果无输出，因此添加try-exception代码块进行检查
    try:  
    
        submission_dict = {
            'title':response_dict.get('title','NO Title'), # 设置默认值，如果无标题就默认无标题
            'hn_link':f"http://news.ycombinator.com/item?id={submission_id}",
            'comments':response_dict.get('descendants',0), #无评论默认为0
        }
        submission_dicts.append(submission_dict)  ## 将穿件的信息都储存到之前的空列表当中
    except Exception as e:
        print(f"处理{submission_id}时出错：{e}")  


# 文章处理完成后再进行排序
submission_dicts = sorted(submission_dicts,key=itemgetter('comments'),
                              reverse=True)
for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")