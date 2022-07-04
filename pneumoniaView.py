# 获取疫情数据，制作可视化地图

import requests
url = 'https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner'
response = requests.get(url=url)
