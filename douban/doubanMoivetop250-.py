# 爬取豆瓣电影TOP250

import requests #数据请求模块
import parsel
import csv
import time # 时间模块

f=open('豆瓣top250.csv',mode='a',encoding='utf-8',newline='')
csv_writer = csv.DictWriter(f,fieldnames=[
        '标题',
        '导演',
        '主演',
        '年份',
        '国家',
        '类型',
        '简介',
        '评分',
        '评价人数',
])
csv_writer.writeheader()

for page in range(0,250,25):
    p = int(page/25+1)
    print(f"开始爬取第{p}页")
    time.sleep(1)
    # 1.发送请求，确定url
    url = f'https://movie.douban.com/top250?start={page}&filter='
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)

    # 2.获取数据
    #print(response.text)

    # 3.解析数据，提取想要的内容
    # 解析数据方法：re正则表达式 / xpath / css选择器
    # 使用parsel解析模块里面css选择器
    # 把获取到的html字符串数据类型进行转换
    selector = parsel.Selector(response.text)

    # css选择器 主要根据标签属性内容提取数据
    lis = selector.css('.grid_view li') # 获取所有的li标签，返回的数据是列表，列表里每一个元素都是selector对象
    for li in lis:
        title = li.css('.info .hd span.title:nth-child(1)::text').get()
        moive_info_list = li.css('.bd p:nth-child(1)::text').getall()
        #getall返回的是列表，strip()去除字符串左右两端空格

        actor_list = moive_info_list[0].strip().split('\xa0\xa0\xa0')
        if len(actor_list) > 1:
            director = actor_list[0].replace('导演: ','') #导演
            actor = actor_list[1].replace('主演: ','').replace('/...','') # 主演
        else:
            director = actor_list[0].replace('导演: ','')
            actor = 'None'
        moive_info = moive_info_list[1].strip().split('\xa0/\xa0')
        moive_year = moive_info[0] # 年份
        moive_con = moive_info[1] # 国家
        moive_type = moive_info[2] # 类型

        moive_brief = li.css('.inq::text').get() # 简介
        moive_scorn = li.css('.rating_num::text').get() # 评分
        moive_comment = li.css('.star span:nth-child(4)::text').get().replace('人评价','') # 评价人数
        dic = {
            '标题':title,
            '导演':director,
            '主演':actor,
            '年份':moive_year,
            '国家':moive_con,
            '类型':moive_type,
            '简介':moive_brief,
            '评分':moive_scorn,
            '评价人数':moive_comment
        }

        csv_writer.writerow(dic)

        print(title,director,actor,moive_year,moive_con,moive_type,moive_brief,moive_scorn,moive_comment,sep='|')
    

