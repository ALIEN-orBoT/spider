# 爬取代理ip
# https://www.kuaidaili.com/free


from time import time
import requests
import re
import parsel
import time

lis = []
lis_1 = []

for page in range(1,15):
    # 1.发送请求
    url = f'https://free.kuaidaili.com/free/inha/{page}/'
    time.sleep(1)
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers) 

    # 2.获取的数据内容
    # print(response.text)

    '''
    # 3.解析数据 方法一：使用正则表达式
    ip_list = re.findall('<td data-title="IP">(.*?)</td>',response.text)
    port_list = re.findall('<td data-title="PORT">(.*?)</td>',response.text)
    '''
    '''
    #方法二：css选择器
    selector =  parsel.Selector(response.text) # 把字符串数据转换成selector对象
    ip_list = selector.css('#list tbody tr td:nth-child(1)::text').getall()
    port_list = selector.css('#list tbody tr td:nth-child(2)::text').getall()
    '''

    # 方法三：xpath
    selector =  parsel.Selector(response.text) # 把字符串数据转换成selector对象
    ip_list = selector.xpath('//*[@id="list"]//tbody/tr/td[1]/text()').getall()
    port_list = selector.xpath('//*[@id="list"]//tbody/tr/td[2]/text()').getall()
    time_list = selector.xpath('//*[@id="list"]//tbody/tr/td[6]/text()').getall()

    for ip, port,resp_time in zip(ip_list,port_list,time_list):
        # print(ip,port)
        proxy = ip+':'+port
        proxies_dict={
            'http':'http://' + proxy,
            'https':'https://' + proxy,
        }
        print(proxies_dict)
        lis.append(proxies_dict)
        
        try:
            response = requests.get(url=url,proxy=proxies_dict,timeout=1)
            if response.status_code == 200:
                print('当前IP代理：',proxies_dict,'可用')
                lis_1.append(proxies_dict)
        except:
            print('当前IP代理：',proxies_dict,"请求超时")

print("获取到的代理ip数量：",len(lis))

print("=====================正在监测代理======================")
print('可用代理：',lis_1)
print('可用代理数量',len(lis_1))