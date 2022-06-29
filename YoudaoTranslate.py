#urllib的使用
#利用有道词典翻译

import urllib.request
import urllib.parse
import json

content = input("输入要翻译的内容：")

url="https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionForm=http://www.youdao.com"
data={}
data['type'] = 'AUTO'
data['i'] = content
data['doctype'] = 'json'
data['xmlVersion'] = '1.6'
data['keyform'] = 'fanyi.web'
data['ue'] = 'UTF-8'
data['typeResult'] = 'true'

data = urllib.parse.urlencode(data).encode('utf-8')
response = urllib.request.urlopen(url,data)

html = response.read().decode('utf-8')
target = json.loads(html)


print(target['translateResult'][0][0]['tgt'])
