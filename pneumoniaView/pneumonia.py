# 获取疫情数据，制作可视化地图

import requests
import re
import json
import csv

with open('data.csv', mode='w',encoding='utf-8',newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(['area','curConfirm','curConfirmRelative','confirmed','crued','died'])

# 发送请求
url = 'https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner'
headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
response = requests.get(url=url,headers=headers)

# 获取数据
html_data = response.text
# print(html_data)

# 解析数据 使用正则表达式
json_str = re.findall('"component":\[(.*)\],',html_data)[0]
#转换类型，将字符串转化为字典
json_dict =json.loads(json_str) 
caseList = json_dict['caseList']
for case in caseList:
    area = case['area']                 # 地区
    curConfirm = case['curConfirm']     # 确诊人数
    curConfirmRelative = case['curConfirmRelative'] # 当前确诊
    confirmed = case['confirmed']       # 累计确诊
    crued = case['crued']               # 治愈人数       
    died = case['died']                 # 死亡人数
    print(area,curConfirm,curConfirmRelative,confirmed,crued,died)
    with open('data.csv', mode='a',encoding='utf-8',newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow([area,curConfirm,curConfirmRelative,confirmed,crued,died])




