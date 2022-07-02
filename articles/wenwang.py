# 爬付费文档 https://www.chinawenwang.com/

import requests
import re
import parsel # 数据解析模块
import os # 文件操作模块
import pdfkit

html_filename = 'articles\\wenwang\\html\\'
if not os.path.exists(html_filename):
    os.mkdir(html_filename)

pdf_filename = 'articles\\wenwang\\pdf\\'
if not os.path.exists(pdf_filename):
    os.mkdir(pdf_filename)

html_str="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    {article}
</body>
</html>
"""
def changer_title(name):
    new_name = re.sub(r'[\\\/\:\*\?\"\,\.\|]','_',name)
    return new_name

# 文章列表的url地址
for page in (1,2):
    url = f'https://www.chinawenwang.com/zlist-37-{page}.html'
    headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
        }
    response = requests.get(url=url, headers=headers)   
    # print(response.text)

    href = re.findall('<a href="(.*?)" class="juhe-page-left-div-link">',response.text)
    for link in href:   
        # 逐个获取文章
        response_1 = requests.get(url=link, headers=headers)
        selector = parsel.Selector(response_1.text)
        title = selector.css('.content-page-header-div h1::text').get()
        name = changer_title(title) # 替换标题中的特殊字符
        content = selector.css('.content-page-main-content-div').get()
        article = html_str.format(article=content)
        html_path = html_filename + name + ".html" 
        pdf_path = pdf_filename + name + ".pdf" 
        try:
            with open(html_path,mode="w",encoding="utf-8") as f:
                f.write(article)
            config = pdfkit.configuration(wkhtmltopdf=r'D:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
            pdfkit.from_file(html_path,pdf_path,configuration=config)
            print("保存成功",name)
        except: 
            pass


